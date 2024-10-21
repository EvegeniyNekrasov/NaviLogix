from pydantic import BaseModel


class TrakingIn(BaseModel):
    container_id: int
    location: str
    timestamp: str
    status: str


class Traking(TrakingIn):
    id: int
