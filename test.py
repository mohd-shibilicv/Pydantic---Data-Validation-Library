from pydantic import ValidationError

from complex_data_validation_lib import validate_user_data, validate_order_data


user_data = {
    "username": "johndoe",
    "email": "john.doe@example.com",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62701",
    },
    "phone_numbers": ["+12345678901"],
}

order_data = {
    "order_id": 1,
    "user": user_data,
    "product_name": "Laptop",
    "quantity": 2,
    "order_date": "2023-01-15",
}

try:
    user = validate_user_data(user_data)
    print("Validated user:", user)

    order = validate_order_data(order_data)
    print("Validated order:", order)
except ValidationError as e:
    print("Validation error:", e)
