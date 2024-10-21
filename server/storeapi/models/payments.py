from pydantic import BaseModel


class PaymentsIn(BaseModel):
    invoice_id: int
    payment_date: str
    amount: float
    method: str
    reference: str


class Payments(PaymentsIn):
    id: int
