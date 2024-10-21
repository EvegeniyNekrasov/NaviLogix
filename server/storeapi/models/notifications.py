from pydantic import BaseModel


class NotificationsIn(BaseModel):
    user_id: int
    message: str
    is_read: int
    timestamp: str


class Notifications(NotificationsIn):
    id: int
