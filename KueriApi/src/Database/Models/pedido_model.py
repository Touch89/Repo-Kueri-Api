from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from src.Database.Models.producto_model import Producto

class Pedido(BaseModel):
    id: int
    tipo: TipoPedido
    estado: EstadoPedido
    productos: list[Producto]
    precio_envio: Optional[float] = None
    precio_total: float
    fecha_creación: str #Ver el equivalente al datetime de otros lenguajes***
    fecha_actualización: str #igual

class TipoPedido(str, Enum):
    en_linea = "virtual"
    fisico = "físico"
  
class EstadoPedido(str, Enum):
    entregado = "entregado"
    en_proceso = "en proceso"
    cancelado = "cancelado"