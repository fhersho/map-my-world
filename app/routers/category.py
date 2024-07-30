from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud import category as crud_category
from app.database import SessionLocal
from app.schemas.category import Category, CategoryCreate

router = APIRouter(prefix="/categories", tags=["categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        db_category = crud_category.create_category(db=db, category=category)
        return db_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{category_id}", response_model=Category, status_code=status.HTTP_200_OK)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud_category.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/", response_model=list[Category], status_code=status.HTTP_200_OK)
def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categories = crud_category.get_categories(db, skip=skip, limit=limit)
    return categories
