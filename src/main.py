from fastapi import FastAPI
from src.routes import user, message, auth
from src.database import Base, engine
from src.utils.middleware import GlobalLogMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.add_middleware(GlobalLogMiddleware)


@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(user.router)
app.include_router(message.router)
app.include_router(auth.router)