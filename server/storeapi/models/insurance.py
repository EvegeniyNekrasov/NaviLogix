from pydantic import BaseModel


class InsuranceIn(BaseModel):
    shipment_id: int
    provider: str
    policy_number: str
    coverage_amount: float
    expiration_date: str


class Insurance(InsuranceIn):
    id: int
