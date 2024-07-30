from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.location_category_reviewed import LocationCategoryReviewed
from app.services.recommender import get_unreviewed_combinations

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[LocationCategoryReviewed], status_code=status.HTTP_200_OK)
def get_recommendations(db: Session = Depends(get_db)):
    try:
        recommendations = get_unreviewed_combinations(db)
        return recommendations
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred while fetching recommendations.")
