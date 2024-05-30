from pydantic import ValidationError
from typing import Dict

from complex_data_validation_lib.models import AddressModel, UserModel, OrderModel


def validate_user_data(data: Dict) -> UserModel:
    try:
        user = UserModel(**data)
        return user
    except ValidationError as e:
        print("User data validation error: ", e)
        raise


def validate_order_data(data: Dict) -> OrderModel:
    try:
        order = OrderModel(**data)
        return order
    except ValidationError as e:
        print("Order data validation error:", e)
        raise
