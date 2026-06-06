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

def get_dashboard_stats(db: Session):

    requests = (
        db.query(MaintenanceRequest)
        .all()
    )

    open_count = len(
        [r for r in requests
         if r.status.value == "OPEN"]
    )

    in_progress_count = len(
        [r for r in requests
         if r.status.value == "IN_PROGRESS"]
    )

    completed_count = len(
        [r for r in requests
         if r.status.value == "COMPLETED"]
    )

    return {
        "open": open_count,
        "in_progress": in_progress_count,
        "completed": completed_count
    }

def assign_technician(
    db: Session,
    request_id: int,
    technician_id: int
):
    request = (
        db.query(MaintenanceRequest)
        .filter(
            MaintenanceRequest.id == request_id
        )
        .first()
    )

    if request:
        request.technician_id = technician_id

        db.commit()
        db.refresh(request)

    return request

def get_dashboard_stats(
    db: Session
):
    requests = (
        db.query(MaintenanceRequest)
        .all()
    )

    return {
        "open": len([
            r for r in requests
            if r.status ==
            RequestStatus.OPEN
        ]),
        "in_progress": len([
            r for r in requests
            if r.status ==
            RequestStatus.IN_PROGRESS
        ]),
        "completed": len([
            r for r in requests
            if r.status ==
            RequestStatus.COMPLETED
        ])
    }