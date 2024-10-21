from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from storeapi.database import database

from storeapi.routers.booking import booking_router
from storeapi.routers.cargo import cargo_router
from storeapi.routers.containers import containers_router
from storeapi.routers.customers import customers_router
from storeapi.routers.documents import documents_router
from storeapi.routers.employees import employees_router
from storeapi.routers.insurance import insurance_router
from storeapi.routers.invoices import invoices_router
from storeapi.routers.maintenance import maintenance_router
from storeapi.routers.notifications import notifications_router
from storeapi.routers.payments import payments_router
from storeapi.routers.ports import ports_router
from storeapi.routers.roles import roles_router
from storeapi.routers.rolesassignments import rolesassignments_router
from storeapi.routers.routes import routes_router
from storeapi.routers.vessels import vessels_router
from storeapi.routers.voyages import voyages_router
from storeapi.routers.schedules import schedules_router
from storeapi.routers.shipments import shipments_router
from storeapi.routers.traking import traking_router
from storeapi.routers.users import users_router


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

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(booking_router)
app.include_router(cargo_router)
app.include_router(containers_router)
app.include_router(customers_router)
app.include_router(documents_router)
app.include_router(employees_router)
app.include_router(insurance_router)
app.include_router(invoices_router)
app.include_router(maintenance_router)
app.include_router(notifications_router)
app.include_router(payments_router)
app.include_router(ports_router)
app.include_router(roles_router)
app.include_router(rolesassignments_router)
app.include_router(routes_router)
app.include_router(vessels_router)
app.include_router(voyages_router)
app.include_router(schedules_router)
app.include_router(shipments_router)
app.include_router(traking_router)
app.include_router(users_router)
