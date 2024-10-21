import logging

from storeapi.database import employees_table, database
from storeapi.models.employees import Employees, EmployeesIn
from storeapi.routers.generic_route import get_crud_router


logger = logging.getLogger(__name__)


employees_router = get_crud_router(
    table=employees_table,
    model_in=EmployeesIn,
    model_out=Employees,
    prefix="employees",
    database=database,
    logger=logger,
)
