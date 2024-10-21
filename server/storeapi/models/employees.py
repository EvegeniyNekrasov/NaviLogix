from pydantic import BaseModel


class EmployeesIn(BaseModel):
    first_name: str
    last_name: str
    position: str
    vessel_id: int
    date_joined: str
    date_left: str


class Employees(EmployeesIn):
    id: int
