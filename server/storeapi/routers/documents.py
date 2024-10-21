import logging

from storeapi.database import documents_table, database
from storeapi.models.documents import Documents, DocumentsIn
from storeapi.routers.generic_route import get_crud_router

logger = logging.getLogger(__name__)

documents_router = get_crud_router(
    table=documents_table,
    model_in=DocumentsIn,
    model_out=Documents,
    prefix="documents",
    database=database,
    logger=logger,
)
