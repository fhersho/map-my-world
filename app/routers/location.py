from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import location as crud_location
from app.database import SessionLocal
from app.schemas.location import Location, LocationCreate

router = APIRouter(prefix="/locations", tags=["locations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Location, status_code=status.HTTP_201_CREATED)
def create_location(location: LocationCreate, db: Session = Depends(get_db)):
    try:
        db_location = crud_location.create_location(db=db, location=location)
        return db_location
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{location_id}", response_model=Location, status_code=status.HTTP_200_OK)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud_location.get_location(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.get("/", response_model=list[Location], status_code=status.HTTP_200_OK)
def read_locations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    locations = crud_location.get_locations(db, skip=skip, limit=limit)
    return locations
