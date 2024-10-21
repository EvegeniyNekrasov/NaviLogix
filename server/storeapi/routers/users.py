from storeapi.database import users_table, database
from storeapi.models.users import Users, UsersIn
from storeapi.routers.generic_route import get_crud_router


users_router = get_crud_router(
    table=users_table,
    model_in=UsersIn,
    model_out=Users,
    prefix="users",
    database=database,
)
