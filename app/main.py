# # from fastapi import FastAPI


# # app = FastAPI()


# # @app.get("/")
# # def read_root():
# #     return {"message": "Hello FastAPI"}


# # ----

# from fastapi import FastAPI
# from app.database import Base, engine
# from app.models import User

# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello FastAPI"}
from fastapi import FastAPI

from app.database import Base, engine
from app.routers import feedbacks, sessions, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rehearsal Feedback API")

app.include_router(users.router)
app.include_router(sessions.router)
app.include_router(feedbacks.router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}