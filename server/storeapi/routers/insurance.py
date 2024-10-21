import logging

from storeapi.database import insurance_table, database
from storeapi.models.insurance import Insurance, InsuranceIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


insurance_router = get_crud_router(
    table=insurance_table,
    model_in=InsuranceIn,
    model_out=Insurance,
    prefix="insurance",
    database=database,
    logger=logger
)
