from storeapi.database import roles_table, database
from storeapi.models.roles import Role, RoleIn
from storeapi.routers.generic_route import get_crud_router


roles_router = get_crud_router(
    table=roles_table,
    model_in=RoleIn,
    model_out=Role,
    prefix="roles",
    database=database,
)
