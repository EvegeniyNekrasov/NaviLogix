from pydantic import BaseModel


class RoutesIn(BaseModel):
    name: str
    origin_port_id: int
    destination_port_id: int
    distance: float


class Routes(RoutesIn):
    id: int
