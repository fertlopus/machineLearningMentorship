from datetime import time, date, datetime
from pydantic import BaseModel, ValidationError, validator, field_validator


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @field_validator("birthdate", mode="before")
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValidationError("Invalid data for the field birth_date.")
        return v


try:
    Person(first_name="AAA", last_name="BBB", birth_date="1800-01-01")
except ValidationError as e:
    print(str(e))
