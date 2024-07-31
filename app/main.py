from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.database import engine, Base
from app.routers import location, category, recommendation, location_category_reviewed

# base_path
Base.metadata.create_all(bind=engine)

app = FastAPI(root_path="/api/v1")

app.include_router(location.router)
app.include_router(category.router)
app.include_router(recommendation.router)
app.include_router(location_category_reviewed.router)


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred with the database."}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
