from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schemas.maintenance_request import (
    RequestCreate,
    RequestResponse
)

from app.crud.maintenance_request import (
    create_request,
    get_requests,
    update_request_status
)

from app.enums.enums import RequestStatus

router = APIRouter(
    prefix="/requests",
    tags=["Requests"]
)

@router.post(
    "",
    response_model=RequestResponse
)
def create_new_request(
    request: RequestCreate,
    db: Session = Depends(get_db)
):
    return create_request(db, request)

@router.get(
    "",
    response_model=list[RequestResponse]
)
def get_all_requests(
    db: Session = Depends(get_db)
):
    return get_requests(db)

@router.put(
    "/{request_id}",
    response_model=RequestResponse
)
def update_status(
    request_id: int,
    status: RequestStatus,
    db: Session = Depends(get_db)
):
    return update_request_status(
        db,
        request_id,
        status
    )

