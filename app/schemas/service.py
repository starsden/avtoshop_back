from datetime import datetime

from pydantic import BaseModel, Field


class ServiceBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    icon: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1)
    price: str = Field(min_length=1, max_length=120)


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    pass


class ServiceResponse(ServiceBase):
    id: int
    created_at: datetime = Field(validation_alias="created_at", serialization_alias="createdAt")
    updated_at: datetime = Field(validation_alias="updated_at", serialization_alias="updatedAt")

    model_config = {"from_attributes": True, "populate_by_name": True}
