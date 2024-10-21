from pydantic import BaseModel


class RoleIn(BaseModel):
    name: str
    description: int


class Role(RoleIn):
    id: int
