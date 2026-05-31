from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.user import User
from app.models.maintenance_request import MaintenanceRequest
from app.routers import users, requests

app = FastAPI(title="Facility Fix")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(requests.router)