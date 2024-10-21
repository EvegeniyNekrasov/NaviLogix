from pydantic import BaseModel


class ContainerIn(BaseModel):
    container_number: str
    status: str
    current_location_port_id: int
    shipment_id: int
    vessel_id: int


class Container(ContainerIn):
    id: int
