import logging

from storeapi.database import tracking_table, database
from storeapi.models.traking import Traking, TrakingIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


traking_router = get_crud_router(
    table=tracking_table,
    model_in=TrakingIn,
    model_out=Traking,
    prefix="traking",
    database=database,
    logger=logger,
)
