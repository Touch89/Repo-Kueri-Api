from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
  from .pedido_model import Pedido
  from .producto_model import Producto

class ProductoPedido(SQLModel, table = True):
    idPedido = int | None = Field(default=None, foreign_key="pedido.id", primary_key=True)
    idProducto = int | None = Field(default=None, foreign_key="producto.id", primary_key=True)
    cantidad = int = Field(default=1)