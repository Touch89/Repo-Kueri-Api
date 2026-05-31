from pydantic import BaseModel, Field
from typing import TYPE_CHECKING, Optional
from datetime import datetime
from enum import Enum
from src.database.models.producto_model import Producto, ProductoEnPedido
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
  from .producto_model import Producto
  from .producto_pedido_model import ProductoPedido

class TipoPedido(str, Enum):
    en_linea = "virtual"
    fisico = "físico"
  
class EstadoPedido(str, Enum):
    entregado = "entregado"
    en_proceso = "en proceso"
    cancelado = "cancelado"

class PedidoBase(SQLModel):
    tipo: TipoPedido
    estado: EstadoPedido
    precio_total: float
    nombre_cliente: Optional[str] = None
    direccion_cliente: Optional[str] = None
    correo_cliente: Optional[str] = None
    precio_envio: Optional[float] = None

class Pedido(PedidoBase, table = True):
    id: Optional[int] = Field(default=None, primary_key= True)
    productos: list[Producto] = Relationship(back_populates="productos", link_model=ProductoPedido)
    fecha_creación: Optional[datetime] = Field(default_factory=datetime.utcnow)
    fecha_actualización: Optional[datetime] = Field(default_factory=datetime.utcnow)

class PedidoVirtual(BaseModel):
    nombre_cliente: str
    direccion_cliente: str
    correo_cliente: str
    precio_envio: float = Field(default=0.0)
    productos: list[ProductoEnPedido]


class PedidoFisico(BaseModel):
    productos: list[ProductoEnPedido]

