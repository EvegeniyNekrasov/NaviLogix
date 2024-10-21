from storeapi.database import schedules_table, database
from storeapi.models.schedules import Schedules, SchedulesIn
from storeapi.routers.generic_route import get_crud_router


schedules_router = get_crud_router(
    table=schedules_table,
    model_in=SchedulesIn,
    model_out=Schedules,
    prefix="schedules",
    database=database,
)
