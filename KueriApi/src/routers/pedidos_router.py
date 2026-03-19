from http.client import OK, HTTPException
from typing import Annotated, Union
from typing import Optional
from pydantic import BaseModel, Field

from fastapi import FastAPI, status, APIRouter, HTTPException

router = APIRouter(
  prefix="/pedidos",)


@router.get("/pedidos",
         description= "Obtiene la lista de pedidos. Se pueden filtrar los productos por su estado o tipo de pedido.",
         tags=["Admin / Pedidos"])
def obtener_pedidos(tipo: Optional[str] = None, estado: Optional[str] = None):
  return

@router.get("/pedidos/{id_pedido}", 
         description="Retorna los datos del pedido que coincida con la id dada.",
         tags=["Admin / Pedidos"])

@router.post("/pedidos/en_linea", status_code=status.HTTP_201_CREATED, 
          description = "Crea un pedido en línea. Requiere del nombre, dirección, correo electrónico.", 
          tags = ["Pedidos"])
def crear_pedido_virtual(nombre: str, direccion: str, correo: str):
  return

#Este lo usan los empleados, falta ver los datos específicos que se piden.
@router.post("pedidos/fisico", status_code=status.HTTP_201_CREATED, 
          description = "Crea un pedido en físico.", 
          tags = ["Admin / Pedidos"]) #Es tanto admin como empleados, pero aún no he hecho la división en ningún endpoint
def crear_pedido_fisico():
  return

@router.put("/pedidos/fisico/{id_pedido}",
          description = "Modifica los datos de un pedido físico.", 
          tags = ["Pedidos"])
def actualizar_pedido_fisico(id: int):
  return

@router.put("/pedidos/en_linea/{id_pedido}",
          description = "Modifica los datos de un pedido en línea.", 
          tags = ["Pedidos"])
def actualizar_pedido_virtual(id: int):
  return

@router.delete("/pedidos/fisico/{id_pedido}",
          description = "Elimina un pedido físico. Para eliminar el pedido tiene que haberse cancelado.", 
          tags = ["Pedidos"])
def eliminar_pedido_fisico(id: int):
  return

@router.delete("/pedidos/en_linea/{id_pedido}",
          description = "Modifica los datos de un pedido en línea. Para eliminarse el pedido tiene que haberse cancelado", 
          tags = ["Pedidos"])
def eliminar_pedido_virtual(id: int):
  return