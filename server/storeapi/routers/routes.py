import logging

from storeapi.database import routes_table, database
from storeapi.models.routes import Routes, RoutesIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


routes_router = get_crud_router(
    table=routes_table,
    model_in=RoutesIn,
    model_out=Routes,
    prefix="routes",
    database=database,
    logger=logger
)
