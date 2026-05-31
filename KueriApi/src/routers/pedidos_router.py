from http.client import OK, HTTPException
from typing import Annotated, Union
from typing import Optional
from pydantic import BaseModel, Field
from src.database.models.pedido_model import PedidoBase, Pedido, TipoPedido, EstadoPedido, PedidoVirtual, PedidoFisico
from src.database.models.producto_model import Producto, ProductoEnPedido
from src.database.models.producto_pedido_model import ProductoPedido
from fastapi import FastAPI, status, APIRouter, HTTPException
from ..dependencies import SessionDep
from typing import Any
from sqlmodel import Field, SQLModel, create_engine, Session, select, col, or_, Relationship

router = APIRouter(
  prefix="/pedidos",)


@router.get("/",
         description= "Obtiene la lista de pedidos. Se pueden filtrar los productos por su estado o tipo de pedido.",
         tags=["Admin / Pedidos"])
def obtener_pedidos(session: SessionDep, tipo: Optional[TipoPedido] = None, estado: Optional[EstadoPedido] = None) -> Any:
  if (tipo is not None and estado is not None):
    statement = select(Pedido).where(Pedido.tipo == tipo, Pedido.estado == estado)
  elif (tipo is not None):
    statement = select(Pedido).where(Pedido.tipo == tipo)
  elif (estado is not None):
    statement = select(Pedido).where(Pedido.estado == estado)
  else:
    statement = select(Pedido)

  pedidos = session.exec(statement).all()

  return pedidos

@router.get("/{id_pedido}", 
         description="Retorna los datos del pedido que coincida con la id dada.",
         tags=["Admin / Pedidos"])
def obtener_pedido(session: SessionDep, id_pedido: int):
  pedido = session.get(Pedido, id_pedido)
  if pedido is None:
    raise HTTPException(status_code=404, detail="El pedido que buscas no existe")
  return pedido

@router.post("/en_linea", status_code=status.HTTP_201_CREATED, 
          description = "Crea un pedido en línea. Requiere del nombre, dirección, correo electrónico.", 
          tags = ["Pedidos"])
def crear_pedido_virtual(session:SessionDep, pedido: PedidoVirtual) -> Pedido:
  pedidoFinal = Pedido(
        tipo = TipoPedido.en_linea,
        estado = EstadoPedido.en_proceso,
        nombre_cliente = pedido.nombre_cliente,
        direccion_cliente = pedido.direccion_cliente,
        correo_cliente = pedido.correo_cliente,
        precio_envio = pedido.precio_envio,
        precio_total = 0
    )
  session.add(pedidoFinal)
  precio_total = 0
  for producto in pedido.productos:
    datosProducto = session.get(Producto, producto.id_producto)
    if datosProducto is None:
      raise HTTPException(status_code=404, detail=f"El producto {producto.id_producto} no existe")
    if datosProducto.stock < producto.cantidad:
      raise HTTPException(status_code = 404, detail = f"El producto {producto.id_producto} no tiene stock suficiente")
    precio_total += (datosProducto.precio * producto.cantidad)
    datosProducto.stock -= producto.cantidad
    conexion = ProductoPedido(
      idPedido = pedidoFinal.id,
      idProducto = producto.id_producto,
      cantidad = producto.cantidad
    )
    session.add(conexion)
  pedidoFinal.precio_total = precio_total + pedidoFinal.precio_envio
  session.commit()
  session.refresh(pedidoFinal)
  return pedidoFinal

#Este lo usan los empleados, falta ver los datos específicos que se piden.
@router.post("/fisico", status_code=status.HTTP_201_CREATED, 
          description = "Crea un pedido en físico.", 
          tags = ["Admin / Pedidos"]) #Es tanto admin como empleados, pero aún no he hecho la división en ningún endpoint
def crear_pedido_fisico(session:SessionDep, pedido: PedidoFisico) -> Pedido: 
  pedidoFinal = Pedido(
        tipo = TipoPedido.fisico,
        estado = EstadoPedido.en_proceso,
        precio_total = 0
    )
  session.add(pedidoFinal)
  precio_total = 0
  for producto in pedido.productos:
    datosProducto = session.get(Producto, producto.id_producto)
    if datosProducto is None:
      raise HTTPException(status_code=404, detail=f"El producto {producto.id_producto} no existe")
    if datosProducto.stock < producto.cantidad:
      raise HTTPException(status_code = 404, detail = f"El producto {producto.id_producto} no tiene stock suficiente")
    precio_total += (datosProducto.precio * producto.cantidad)
    datosProducto.stock -= producto.cantidad
    conexion = ProductoPedido(
      idPedido = pedidoFinal.id,
      idProducto = producto.id_producto,
      cantidad = producto.cantidad
    )
    session.add(conexion)
  pedidoFinal.precio_total = precio_total
  session.commit()
  session.refresh(pedidoFinal)
  return pedidoFinal

@router.put("/fisico/{id_pedido}",
          description = "Modifica los datos de un pedido físico.", 
          tags = ["Pedidos"])
def actualizar_pedido_fisico(id_pedido: int):
  return

@router.put("/en_linea/{id_pedido}",
          description = "Modifica los datos de un pedido en línea.", 
          tags = ["Pedidos"])
def actualizar_pedido_virtual(id_pedido: int):
  return

@router.delete("/{id_pedido}",
          description = "Elimina un pedido físico. Para eliminar el pedido tiene que haberse cancelado.", 
          tags = ["Pedidos"])
def eliminar_pedido(session: SessionDep, id_pedido: int):
  pedido = session.get(Pedido, id_pedido)
  if pedido is None:
    raise HTTPException(status_code = 404, detail = f"El pedido (id: {id_pedido}) no existe")
  if pedido.estado != EstadoPedido.cancelado:
    raise HTTPException(status_code = 400, detail = f"El pedido (id: {id_pedido}) no puede ser eliminado") 
  session.delete(pedido)
  session.commit()
  response = f"El pedido (id: {id_pedido}) ha sido eliminado."
  return response