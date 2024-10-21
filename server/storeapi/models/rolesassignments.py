from pydantic import BaseModel


class RolesAssignmentsIn(BaseModel):
    user_id: int
    role_id: int


class RolesAssignments(RolesAssignmentsIn):
    id: int
