from datetime import datetime

from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    text: str = Field(min_length=1)
    rating: int = Field(ge=1, le=5)


class ReviewCreate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    id: int
    status: str
    created_at: datetime = Field(validation_alias="created_at", serialization_alias="createdAt")
    updated_at: datetime = Field(validation_alias="updated_at", serialization_alias="updatedAt")

    model_config = {"from_attributes": True, "populate_by_name": True}
