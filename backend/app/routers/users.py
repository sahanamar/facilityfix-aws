from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.user import get_user_by_email

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.crud.user import (
    create_user,
    get_users,
    get_user,
    get_user_by_email
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponse
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@router.get(
    "",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db)
):
    return get_users(db)

@router.get(
    "/email/{email}",
    response_model=UserResponse
)
def get_user_using_email(
    email: str,
    db: Session = Depends(get_db)
):
    return get_user_by_email(
        db,
        email
    )
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_single_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user(db, user_id)

