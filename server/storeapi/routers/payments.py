import logging

from storeapi.database import payments_table, database
from storeapi.models.payments import Payments, PaymentsIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


payments_router = get_crud_router(
    table=payments_table,
    model_in=PaymentsIn,
    model_out=Payments,
    prefix="payments",
    database=database,
    logger=logger
)
