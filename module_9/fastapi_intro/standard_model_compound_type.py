from pydantic import BaseModel, ValidationError
from datetime import date
from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date | None = None
    interests: list[str]

    def __str__(self):
        return (f"Person:\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\n"
                f"age: {self.age}\nweight: {self.weight}")


try:
    Person(
        first_name="Adam",
        last_name="Adamov",
        gender=Gender.MALE,
        birthdate="1991-01-01",
        interests=["music", "reading"],
    )
except ValidationError as e:
    print(str(e))


print(Person)
