from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import user  # # noqa: F401 


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "LifeOS Backend Running"}
