from pydantic import BaseModel

class PortsIn(BaseModel):
    name: str
    country: str
    code: str
    latitude: float
    longitude: float
    timezone: str


class Ports(PortsIn):
    id: int