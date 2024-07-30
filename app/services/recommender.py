from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models.location_category_reviewed import LocationCategoryReviewed


def get_unreviewed_combinations(db: Session, days: int = 30, limit: int = 10):
    threshold_date = datetime.utcnow() - timedelta(days=days)
    reviewed = (db.query(LocationCategoryReviewed).filter(
        LocationCategoryReviewed.last_reviewed < threshold_date)
                .order_by(LocationCategoryReviewed.last_reviewed)
                .limit(limit).all())
    return reviewed
