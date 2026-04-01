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
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import Base, SessionLocal, engine
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.post("/users")
def create_user(name: str, db: Session = Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"id": user.id, "name": user.name}


@app.get("/users")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users