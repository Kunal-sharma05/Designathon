from fastapi import FastAPI

import models
from db.database import engine
from routers.user import router
from db.database import base

app = FastAPI()

base.metadata.create_all(bind=engine)


app.include_router(router,tags=["User"])