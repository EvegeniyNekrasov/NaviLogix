import logging

from storeapi.database import cargo_table, database
from storeapi.models.cargo import Cargo, CargoIn
from storeapi.routers.generic_route import get_crud_router

logger = logging.getLogger(__name__)

cargo_router = get_crud_router(
    table=cargo_table,
    model_in=CargoIn,
    model_out=Cargo,
    prefix="cargo",
    database=database,
    logger=logger,
)
