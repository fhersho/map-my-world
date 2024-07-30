from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.location_category_reviewed import LocationCategoryReviewed
from app.schemas.location_category_reviewed import LocationCategoryReviewedCreate


def get_location_category_reviewed(db: Session, reviewed_id: int):
    return db.query(LocationCategoryReviewed).filter(LocationCategoryReviewed.id == reviewed_id).first()


def get_reviewed_combinations(db: Session, days: int = 30):
    threshold_date = datetime.utcnow() - timedelta(days=days)
    return db.query(LocationCategoryReviewed).filter(LocationCategoryReviewed.last_reviewed < threshold_date).all()


def create_reviewed_combination(db: Session, reviewed: LocationCategoryReviewedCreate):
    db_reviewed = LocationCategoryReviewed(**reviewed.dict())
    db.add(db_reviewed)
    db.commit()
    db.refresh(db_reviewed)
    return db_reviewed
