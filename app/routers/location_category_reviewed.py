from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.location_category_reviewed import LocationCategoryReviewed, LocationCategoryReviewedCreate

router = APIRouter(
    prefix="/location-category-reviewed",
    tags=["location_category_reviewed"],
    responses={404: {"description": "Not Found"}}
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=LocationCategoryReviewed, status_code=status.HTTP_201_CREATED)
def create_location_category_reviewed(review: LocationCategoryReviewedCreate, db: Session = Depends(get_db)):
    return crud.create_location_category_reviewed(db=db, review=review)


@router.get("/{review_id}", response_model=LocationCategoryReviewed)
def read_location_category_reviewed(review_id: int, db: Session = Depends(get_db)):
    db_review = crud.get_location_category_reviewed(db=db, review_id=review_id)
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review


@router.get("/", response_model=list[LocationCategoryReviewed])
def read_location_category_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_location_category_reviews(db=db, skip=skip, limit=limit)
