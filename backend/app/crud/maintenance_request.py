from sqlalchemy.orm import Session

from app.models.maintenance_request import MaintenanceRequest
from app.schemas.maintenance_request import RequestCreate
from app.enums.enums import RequestStatus

def create_request(
    db: Session,
    request: RequestCreate
):
    db_request = MaintenanceRequest(
        title=request.title,
        description=request.description,
        priority=request.priority,
        status=RequestStatus.OPEN,
        user_id=request.user_id
    )

    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return db_request

def get_requests(db: Session):
    return (
        db.query(MaintenanceRequest)
        .all()
    )

def update_request_status(
    db: Session,
    request_id: int,
    status: RequestStatus
):
    request = (
        db.query(MaintenanceRequest)
        .filter(
            MaintenanceRequest.id == request_id
        )
        .first()
    )

    if request:
        request.status = status

        db.commit()
        db.refresh(request)

    return request

