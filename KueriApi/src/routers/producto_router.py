from http.client import OK, HTTPException
from typing import Annotated, Union
from typing import Optional
from pydantic import BaseModel, Field

from fastapi import FastAPI, status, APIRouter, HTTPException

router = APIRouter(
  prefix="/productos",)

#Sección Productos (Tanto admin/empleados como usuarios)

@router.get("/")
def read_root():
  return {"Hello": "World"}

@router.get("/productos", description = "Obtiene todos los productos disponibles", tags= ["Productos"])
def obtener_productos():
  return

@router.get("/productos/{id_producto}", description = "Retorna los datos del producto que coincida con la id dada", 
         tags= ["Productos"])
def obtener_producto(id_producto: int):
  return

@router.get("/productos/{nombre}", description = "Retorna los productos que coincidan con el nombre dado.", 
         tags= ["Productos"])
def obtener_producto(nombre: str):
  return

@router.post("/productos", status_code=status.HTTP_201_CREATED,
          description = "Crea un producto nuevo. Requiere del nombre, descripción, imagen(por ahora), precio y SKU del producto. Únicamente puede ser usado por administradores.",
          tags=["Admin / Productos"]) 
def crear_producto(nombre: str, descripcion: str, precio: float, sku: str):
  return

@router.delete("/productos/{id_producto}", description = 
            """
            Elimina un producto de la lista de productos disponibles. 
            El producto no puede ser eliminado si hay pedidos en proceso que contengan el producto a eliminar.
            """, tags=["Admin / Productos"])
def eliminar_producto(id_producto: int):
  return

@router.put("/productos/{id_producto}", description = "Actualiza los datos de un producto con los datos dados. No se puede dejar datos vacíos al actualizar el producto. Únicamente puede ser usado por administradores.",
         tags=["Admin / Productos"])
def actualizar_producto(id_producto: int):
  return