from datetime import date


def validate_positive(value: int) -> int:
    if value <= 0:
        raise ValueError("Value must be positive")
    return value


def validate_date_in_past(value: date) -> date:
    if value >= date.today():
        raise ValueError("Date must be in the past")
    return value
