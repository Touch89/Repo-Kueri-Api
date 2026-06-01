from src.database.models.producto_model import Producto
from src.database.models.pedido_model import Pedido
from src.database.models.producto_pedido_model import ProductoPedido

from sqlmodel import SQLModel, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)