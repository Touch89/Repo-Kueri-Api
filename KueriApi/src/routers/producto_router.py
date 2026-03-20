from http.client import OK, HTTPException
from typing import Annotated, Union
from typing import Optional
from pydantic import BaseModel, Field
from src.database.models.producto_model import Producto, ProductoBase
from ..dependencies import SessionDep
from typing import Any
from sqlmodel import Field, SQLModel, create_engine, Session, select, col, or_, Relationship

from fastapi import FastAPI, status, APIRouter, HTTPException

router = APIRouter(
  prefix="/productos",)

#Sección Productos (Tanto admin/empleados como usuarios)

@router.get("/", description = "Obtiene todos los productos disponibles", tags= ["Productos"])
def obtener_productos(session: SessionDep) -> Any: 
  statement = select(Producto)
  results = session.exec(statement)
  productos = results.all()
  return productos

@router.get("/{id_producto}", description = "Retorna los datos del producto que coincida con la id dada", 
         tags= ["Productos"])
def obtener_producto(id_producto: int, session: SessionDep):
  producto = session.get(Producto, id)
  if producto is None:
    raise HTTPException(status_code=404, detail="El producto que buscas no existe")
  return producto

@router.get("/{nombre}", description = "Retorna los productos que coincidan con el nombre dado.", 
         tags= ["Productos"])
def obtener_producto(nombre: str, session: SessionDep):
  statement = select(Producto).where(col(Producto.nombre).contains(nombre))
  results = session.exec(statement).all()
  return results

@router.post("/", status_code=status.HTTP_201_CREATED,
          description = "Crea un producto nuevo. Requiere del nombre, descripción, imagen(por ahora), precio y SKU del producto. Únicamente puede ser usado por administradores.",
          tags=["Admin / Productos"], response_model = Producto) 
def crear_producto(producto: ProductoBase, session: SessionDep) -> Producto:
  productoNuevo = Producto.model_validate(producto)
  session.add(productoNuevo)
  session.commit()
  session.refresh(productoNuevo)
  return productoNuevo

@router.delete("/{id_producto}", description = 
            """
            Elimina un producto de la lista de productos disponibles. 
            El producto no puede ser eliminado si hay pedidos en proceso que contengan el producto a eliminar.
            """, tags=["Admin / Productos"])
def eliminar_producto(id_producto: int):
  return

@router.put("/{id_producto}", description = "Actualiza los datos de un producto con los datos dados. No se puede dejar datos vacíos al actualizar el producto. Únicamente puede ser usado por administradores.",
         tags=["Admin / Productos"])
def actualizar_producto(id_producto: int):
  return