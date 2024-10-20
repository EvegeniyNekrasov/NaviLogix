from contextlib import asynccontextmanager

from fastapi import FastAPI

from storeapi.database import database
from storeapi.routers.test import router as test_router
from storeapi.routers.ports import router as port_router


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


app.include_router(test_router)
app.include_router(port_router)
