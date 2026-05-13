from pydantic import BaseModel, Field

class Carrito(BaseModel):
    id: int
    productos: list
    total: float
    