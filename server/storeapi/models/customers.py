from pydantic import BaseModel


class CustomersIn(BaseModel):
    name: str
    address: str
    phone: str
    email: str
    contact_person: str


class Customers(CustomersIn):
    id: int
