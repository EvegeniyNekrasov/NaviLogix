from storeapi.database import voyages_table, database
from storeapi.models.voyages import VouyagesIn, Voyages
from storeapi.routers.generic_route import get_crud_router


voyages_router = get_crud_router(
    table=voyages_table,
    model_in=VouyagesIn,
    model_out=Voyages,
    prefix="voyages",
    database=database,
)
