from http.client import OK, HTTPException
from typing import Annotated, Union
from typing import Optional
from pydantic import BaseModel, Field

from fastapi import FastAPI, status

app = FastAPI()


#Sección Productos (Tanto admin/empleados como usuarios)

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/productos", description = "Obtiene todos los productos disponibles", tags= ["Productos"])
def obtener_productos():
  return

@app.get("/productos/{id_producto}", description = "Retorna los datos del producto que coincida con la id dada", 
         tags= ["Productos"])
def obtener_producto(id_producto: int):
  return

@app.get("/productos/{nombre}", description = "Retorna los productos que coincidan con el nombre dado.", 
         tags= ["Productos"])
def obtener_producto(nombre: str):
  return

@app.post("/productos", status_code=status.HTTP_201_CREATED,
          description = "Crea un producto nuevo. Requiere del nombre, descripción, imagen(por ahora), precio y SKU del producto. Únicamente puede ser usado por administradores.",
          tags=["Admin / Productos"]) 
def crear_producto(nombre: str, descripcion: str, precio: float, sku: str):
  return

@app.delete("/productos/{id_producto}", description = 
            """
            Elimina un producto de la lista de productos disponibles. 
            El producto no puede ser eliminado si hay pedidos en proceso que contengan el producto a eliminar.
            """, tags=["Admin / Productos"])
def eliminar_producto(id_producto: int):
  return

@app.put("/productos/{id_producto}", description = "Actualiza los datos de un producto con los datos dados. No se puede dejar datos vacíos al actualizar el producto. Únicamente puede ser usado por administradores.",
         tags=["Admin / Productos"])
def actualizar_producto(id_producto: int):
  return


#Sección Pedidos (Lo mismo)

@app.get("/pedidos",
         description= "Obtiene la lista de pedidos. Se pueden filtrar los productos por su estado o tipo de pedido.",
         tags=["Admin / Pedidos"])
def obtener_pedidos(tipo: Optional[str] = None, estado: Optional[str] = None):
  return

@app.get("/pedidos/{id_pedido}", 
         description="Retorna los datos del pedido que coincida con la id dada.",
         tags=["Admin / Pedidos"])

@app.post("/pedidos/en_linea", status_code=status.HTTP_201_CREATED, 
          description = "Crea un pedido en línea. Requiere del nombre, dirección, correo electrónico.", 
          tags = ["Pedidos"])
def crear_pedido_virtual(nombre: str, direccion: str, correo: str):
  return

#Este lo usan los empleados, falta ver los datos específicos que se piden.
@app.post("pedidos/fisico", status_code=status.HTTP_201_CREATED, 
          description = "Crea un pedido en físico.", 
          tags = ["Admin / Pedidos"]) #Es tanto admin como empleados, pero aún no he hecho la división en ningún endpoint
def crear_pedido_fisico():
  return

@app.put("/pedidos/fisico/{id_pedido}",
          description = "Modifica los datos de un pedido físico.", 
          tags = ["Pedidos"])
def actualizar_pedido_fisico(id: int):
  return

@app.put("/pedidos/en_linea/{id_pedido}",
          description = "Modifica los datos de un pedido en línea.", 
          tags = ["Pedidos"])
def actualizar_pedido_virtual(id: int):
  return

@app.delete("/pedidos/fisico/{id_pedido}",
          description = "Elimina un pedido físico. Para eliminar el pedido tiene que haberse cancelado.", 
          tags = ["Pedidos"])
def eliminar_pedido_fisico(id: int):
  return

@app.delete("/pedidos/en_linea/{id_pedido}",
          description = "Modifica los datos de un pedido en línea. Para eliminarse el pedido tiene que haberse cancelado", 
          tags = ["Pedidos"])
def eliminar_pedido_virtual(id: int):
  return

# Sección Carrito ('')

@app.get("/carrito", 
         description="Obtiene todos los productos en el carrito del usuario.",
         tags=["Carrito"])
def obtener_carrito():
  return

#Hay que ver si es más fácil que use el producto o la id, 
# o capaz y se cambia la dirección completamente
@app.post("/carrito/{id_producto}", status_code=status.HTTP_201_CREATED,
         description = "Agrega un producto al carrito",
         tags=["Carrito"])
def carrito_agregar_producto(id_producto: int):
  return

@app.put("/carrito/{id_producto}",
         description = "Modifica un producto dentro del carrito. Hasta ahora únicamente se puede modificar la cantidad del producto que se pidió",
         tags=["Carrito"])
def carrito_modificar_producto(id_producto: int):
  return

@app.delete("/carrito/{id_producto}", 
            description= "Elimina un producto del carrito",
            tags=["Carrito"])
def carrito_eliminar_producto(id_producto: int):
  return

@app.delete("/carrito", 
            description= "Elimina todos los productos del carrito",
            tags=["Carrito"])
def limpiar_carrito(id_producto: int):
  return



#@app.post("/CrearUsuario", status_code=status.HTTP_201_CREATED)
# def create_user(usuario: BaseUser) -> User:
 # nuevo_id = app.state.last_id + 1
  #nuevo_usuario = User(Nombre=usuario.Nombre, id=nuevo_id)
  #app.state.usuarios.append(nuevo_usuario)
  #app.state.last_id = nuevo_id
  #return nuevo_usuario

#app.get("/usuarios/")
# def get_users(initial_id: int = 0) -> list[User]:
#  usuarios: list[User] = app.state.usuarios
#  resultado = [usuario for usuario in usuarios if usuario.id >= initial_id]
#  return resultado

#app.get("/usuarios/{user_id}")
# def get_user(user_id: int) -> User:
#  usuarios: list[User] = app.state.usuarios
#  usuarios_encontrados = [usuario for usuario in usuarios if usuario.id == user_id][0]
#  if (len.usuarios_encontrados) == 0:
#    return HTTPException(status_code=404, detail="Usuario no encontrado")
#  return usuarios_encontrados[0]

#@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None): 
#  return {"item_id": item_id, "q": q}