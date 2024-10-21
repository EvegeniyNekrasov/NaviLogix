from pydantic import BaseModel


class InvoicesIn(BaseModel):
    customer_id: int
    shipment_id: int
    amount: float
    due_date: str
    status: str


class Invoices(InvoicesIn):
    id: int
