from storeapi.database import ports_table, database
from storeapi.models.ports import Ports, PortsIn
from storeapi.routers.generic_route import get_crud_router


ports_router = get_crud_router(
    table=ports_table,
    model_in=PortsIn,
    model_out=Ports,
    prefix="ports",
    database=database,
)