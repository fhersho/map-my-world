from sqlalchemy.orm import Session

from app.models.location import Location
from app.schemas.location import LocationCreate


def get_location(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()


def get_locations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Location).offset(skip).limit(limit).all()


def create_location(db: Session, location: LocationCreate):
    db_location = Location(latitude=location.latitude, longitude=location.longitude)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
