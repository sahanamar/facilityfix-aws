from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base
from app.database import engine

from app.models.user import User
from app.models.maintenance_request import MaintenanceRequest
from app.routers import users, requests

app = FastAPI(title="Facility Fix")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(requests.router)

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000,"
                                  "http://localhost:5173"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )