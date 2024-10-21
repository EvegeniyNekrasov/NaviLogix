import logging

from storeapi.database import customers_table, database
from storeapi.models.customers import Customers, CustomersIn
from storeapi.routers.generic_route import get_crud_router

logger = logging.getLogger(__name__)


customers_router = get_crud_router(
    table=customers_table,
    model_in=CustomersIn,
    model_out=Customers,
    prefix="customers",
    database=database,
    logger=logger,
)
