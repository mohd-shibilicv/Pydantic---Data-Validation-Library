from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    ValidationError,
    field_validator,
    model_validator,
)
from typing import List, Optional
from datetime import date

from complex_data_validation_lib.validators import (
    validate_positive,
    validate_date_in_past,
)


class AddressModel(BaseModel):
    street: str = Field(..., min_length=1, max_length=100)
    city: str = Field(..., min_length=1, max_length=100)
    state: str = Field(
        ..., min_length=2, max_length=2, description="State abbreviation, e.g., KL"
    )
    zip_code: str = Field(
        ..., pattern=r"^\d{5}(?:-\d{4})?$", description="e.g, 12345-1234"
    )


class UserModel(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0)
    address: AddressModel
    phone_numbers: Optional[List[str]] = None

    @field_validator("username")
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric")
        return value

    @model_validator(mode="before")
    def validate_user(cls, values):
        if values.get("age") < 18:
            raise ValueError("User must be at least 18 years old")
        return values


class OrderModel(BaseModel):
    order_id: int
    user: UserModel
    product_name: str
    quantity: int = Field(..., gt=0)
    order_date: date

    @field_validator("order_id")
    def check_positive_order_id(cls, value):
        return validate_positive(value)

    @field_validator("order_date")
    def check_order_date(cls, value):
        return validate_date_in_past(value)
