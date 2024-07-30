from pydantic import BaseModel


class LocationBase(BaseModel):
    latitude: float
    longitude: float


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
