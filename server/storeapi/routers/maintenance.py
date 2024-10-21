import logging

from storeapi.database import maintenance_table, database
from storeapi.models.maintenance import Maintanance, MaintananceIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


maintenance_router = get_crud_router(
    table=maintenance_table,
    model_in=MaintananceIn,
    model_out=Maintanance,
    prefix="maintenance",
    database=database,
    logger=logger
)
