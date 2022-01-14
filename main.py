import uvicorn
from fastapi.applications import FastAPI
from starlette.middleware.cors import CORSMiddleware

import controllers.user
from models.database import engine, Base

Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    """
    Create the FastAPI application.
    """
    app = FastAPI()
    origins = ["http://localhost:3000", "http://localhost:8080"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    Base.metadata.create_all(bind=engine)
    app.include_router(controllers.user.route, prefix="/user")
    return app


apps = create_app()


@apps.get("/status")
async def home():
    return {"error": False, "version": "0.0.1"}


if __name__ == "__main__":
    uvicorn.run(apps, host="0.0.0.0", port=8000)
