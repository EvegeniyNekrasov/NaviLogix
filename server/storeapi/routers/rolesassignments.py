from storeapi.database import role_assignments_table, database
from storeapi.models.rolesassignments import RolesAssignments, RolesAssignmentsIn
from storeapi.routers.generic_route import get_crud_router


rolesassignments_router = get_crud_router(
    table=role_assignments_table,
    model_in=RolesAssignmentsIn,
    model_out=RolesAssignments,
    prefix="rolesassignments",
    database=database,
)
