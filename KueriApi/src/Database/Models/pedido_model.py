from pydantic import BaseModel, Field
from typing import TYPE_CHECKING, Optional
from datetime import datetime
from enum import Enum
from src.database.models.producto_model import Producto
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
    precio_envio: Optional[float] = None
    precio_total: float
    fecha_creación: datetime = Field(default_factory=datetime.utcnow)
    fecha_actualización: datetime = Field(default_factory=datetime.utcnow)

class Pedido(PedidoBase, table = True):
    id: int = Field(default=None, primary_key= True)
    productos: list[Producto] = Relationship(back_populates="productos", link_model=ProductoPedido)

