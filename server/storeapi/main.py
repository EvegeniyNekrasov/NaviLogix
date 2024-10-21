from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from storeapi.database import database

from storeapi.database import (
    ports_table,
    vessels_table,
    customers_table, 
    database,
)

from storeapi.models.customers import (Customers, CustomersIn)
from storeapi.models.ports import (Ports, PortsIn)
from storeapi.models.vessels import (Vessels, VesselsIn)

from storeapi.routers.generic_route import get_crud_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # conección a la bbdd
    await database.connect()
    # se para hasta que FastAPI le indica que siga
    yield
    # se disconecta de la bbdd
    await database.disconnect()


# Antes de hacer cualquier respuesta tenemos que
# establecer la connceción con la bbdd
app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

customers_router = get_crud_router(
    table=customers_table,
    model_in=CustomersIn,
    model_out=Customers,
    prefix="customers",
    database=database
)

ports_router = get_crud_router(
    table=ports_table,
    model_in=PortsIn,
    model_out=Ports,
    prefix="ports",
    database=database
)

vessels_router = get_crud_router(
    table=vessels_table,
    model_in=VesselsIn,
    model_out=Vessels,
    prefix="vessels",
    database=database
)

app.include_router(ports_router)
app.include_router(vessels_router)
app.include_router(customers_router)
