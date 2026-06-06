from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict

from app.enums.enums import Priority
from app.enums.enums import RequestStatus



class RequestCreate(BaseModel):
    title: str
    description: str
    priority: Priority
    user_id: int

class RequestResponse(BaseModel):
    id: int
    title: str
    description: str

    priority: Priority
    status: RequestStatus

    created_at: datetime

    user_id: int
    technician_id: int | None

    model_config = ConfigDict(
        from_attributes=True
    )

class TechnicianAssignment(BaseModel):
    technician_id: int

class DashboardStats(BaseModel):
    open: int
    in_progress: int
    completed: int