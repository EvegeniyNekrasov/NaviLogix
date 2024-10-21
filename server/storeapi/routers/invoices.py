from storeapi.database import invoices_table, database
from storeapi.models.invoices import Invoices, InvoicesIn
from storeapi.routers.generic_route import get_crud_router


invoices_router = get_crud_router(
    table=invoices_table,
    model_in=InvoicesIn,
    model_out=Invoices,
    prefix="invoices",
    database=database,
)
