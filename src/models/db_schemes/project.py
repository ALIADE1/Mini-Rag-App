from pydantic.v1 import ArbitraryTypeError
from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import objectid


class project(BaseModel):
    _id: Optional[objectid]
    project_id: str = Field(..., min_length=1)

    @validator("project_id")
    def validate_project_id(cls, value):
        if not value.isnalnum():
            raise ValueError("project_id must be alohanumeric")

        return value

    class config:
        arbitrary_types_allowed = True
