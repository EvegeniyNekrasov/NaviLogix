from pydantic import BaseModel


class SchedulesIn(BaseModel):
    voyage_id: int
    port_id: int
    arrival_date: str
    departure_date: str


class Schedules(SchedulesIn):
    id: int
