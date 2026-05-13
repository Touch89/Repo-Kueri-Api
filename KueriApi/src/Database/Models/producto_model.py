from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

class ProductoBase(SQLModel):
    nombre: str = Field(index=True)
    descripcion: str
    imagen_url: str  #Hay que ver cómo implementar
    precio: float
    sku: str
    stock: int

class Producto(ProductoBase, table = True):
    id: Optional[int] = Field(default=None, primary_key= True)
    #fecha_creación: str #Ver el equivalente al datetime acá  
    #fecha_actualización: str #Lo mismo
    