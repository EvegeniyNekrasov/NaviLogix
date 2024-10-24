import logging

from storeapi.database import shipments_table, database
from storeapi.models.shipments import Shipments, ShipmentsIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


shipments_router = get_crud_router(
    table=shipments_table,
    model_in=ShipmentsIn,
    model_out=Shipments,
    prefix="shipments",
    database=database,
    logger=logger
)
