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
from app.routers import feedbacks, sessions, users, pages, videos
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Rehearsal Feedback API")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(users.router)
app.include_router(sessions.router)
app.include_router(feedbacks.router)

## html페이지 띄워주는 라우터
app.include_router(pages.router)
app.include_router(videos.router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}