from datetime import datetime

from pydantic import BaseModel


class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int
    last_reviewed: datetime


class LocationCategoryReviewedCreate(LocationCategoryReviewedBase):
    pass


class LocationCategoryReviewed(LocationCategoryReviewedBase):
    id: int

    class Config:
        orm_mode = True