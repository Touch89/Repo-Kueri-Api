from pydantic import BaseModel, Field

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    #imagen_url: str Hay que ver cómo se van a implementar las imágenes
    precio: float
    sku: str
    stock: int
    fecha_creación: str #Ver el equivalente al datetime acá  
    fecha_actualización: str #Lo mismo