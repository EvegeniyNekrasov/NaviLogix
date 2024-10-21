from pydantic import BaseModel


class CargoIn(BaseModel):
    shipment_id: int
    description: str
    weight: float
    volume: float
    quantity: int


class Cargo(CargoIn):
    id: int
