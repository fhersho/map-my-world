from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.location_category_reviewed import LocationCategoryReviewed
from app.schemas.location_category_reviewed import LocationCategoryReviewedCreate


def create_location_category_reviewed(db: Session, review: LocationCategoryReviewedCreate):
    db_review = LocationCategoryReviewed(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_location_category_reviewed(db: Session, review_id: int):
    return db.query(LocationCategoryReviewed).filter(LocationCategoryReviewed.id == review_id).first()


def get_location_category_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LocationCategoryReviewed).offset(skip).limit(limit).all()


def get_recommendations(db: Session, days: int = 30, limit: int = 10):
    threshold_date = datetime.utcnow() - timedelta(days=days)
    reviews = db.query(LocationCategoryReviewed) \
        .filter(LocationCategoryReviewed.reviewed_at < threshold_date) \
        .order_by(LocationCategoryReviewed.reviewed_at.asc()) \
        .limit(limit).all()
    return reviews
