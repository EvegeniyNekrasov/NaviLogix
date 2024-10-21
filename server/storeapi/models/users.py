from pydantic import BaseModel


class UsersIn(BaseModel):
    username: str
    password: str
    role: str
    employee_id: int


class Users(UsersIn):
    id: int
