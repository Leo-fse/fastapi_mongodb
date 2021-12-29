# flake8 noqa: F401
import uvicorn
from fastapi import FastAPI

from routers.test import test
from routers.user import user

app = FastAPI()


# app.include_router(user)
app.include_router(test)
