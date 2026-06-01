from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from pydantic import BaseModel

from .producto_pedido_model import ProductoPedido

if TYPE_CHECKING:
  from .pedido_model import Pedido

class ProductoBase(SQLModel):
    nombre: str = Field(index=True)
    descripcion: str
    imagen_url: str  #Hay que ver cómo implementar
    precio: float
    sku: str
    stock: int
    categoria: Optional[str] = None

class Producto(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True, sa_column_kwargs={"autoincrement": True})
    nombre: str = Field(index=True)
    descripcion: str
    imagen_url: str  #Hay que ver cómo implementar
    precio: float
    sku: str
    stock: int
    categoria: Optional[str] = Field(default="Sin Categoría", index=True)
    fecha_creacion: Optional[datetime] = Field(default_factory=datetime.utcnow)
    fecha_actualizacion: Optional[datetime] = Field(default_factory=datetime.utcnow)
    pedidos: list["Pedido"] = Relationship(back_populates="productos", link_model=ProductoPedido)


class ProductoEnPedido(BaseModel):
   id_producto: int
   cantidad: int