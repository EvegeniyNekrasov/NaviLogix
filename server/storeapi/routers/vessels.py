from storeapi.database import vessels_table, database
from storeapi.models.vessels import Vessels, VesselsIn
from storeapi.routers.generic_route import get_crud_router


vessels_router = get_crud_router(
    table=vessels_table,
    model_in=VesselsIn,
    model_out=Vessels,
    prefix="vessels",
    database=database,
)
