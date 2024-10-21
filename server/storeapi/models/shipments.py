from pydantic import BaseModel


class ShipmentsIn(BaseModel):
    name: str
    customer_id: int
    booking_number: str
    origin_port_id: int
    destination_port_id: int
    cargo_description: str
    weight: float
    volume: float
    number_of_containers: int
    status: str


class Shipments(ShipmentsIn):
    id: int
