import logging

from storeapi.database import bookings_table, database
from storeapi.models.booking import Booking, BookingIn
from storeapi.routers.generic_route import get_crud_router

logger = logging.getLogger(__name__)

booking_router = get_crud_router(
    table=bookings_table,
    model_in=BookingIn,
    model_out=Booking,
    prefix="booking",
    database=database,
    logger=logger
)
