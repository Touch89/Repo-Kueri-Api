from fastapi import FastAPI, Depends
from fastapi.concurrency import asynccontextmanager
from src.database.database import create_db_and_tables, engine
#from src.routers import carrito_router
from src.routers import pedidos_router
from src.routers import producto_router
from src.dependencies import get_session
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db_and_tables()
  yield

app = FastAPI(lifespan=lifespan, dependencies =[Depends(get_session)])

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#app.include_router(carrito_router.router)
app.include_router(pedidos_router.router)
app.include_router(producto_router.router)
