import logging

from storeapi.database import notifications_table, database
from storeapi.models.notifications import Notifications, NotificationsIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


notifications_router = get_crud_router(
    table=notifications_table,
    model_in=NotificationsIn,
    model_out=Notifications,
    prefix="notifications",
    database=database,
    logger=logger
)
