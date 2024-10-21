from storeapi.database import containers_table, database
from storeapi.models.containers import Container, ContainerIn
from storeapi.routers.generic_route import get_crud_router


containers_router = get_crud_router(
    table=containers_table,
    model_in=ContainerIn,
    model_out=Container,
    prefix="containers",
    database=database,
)
