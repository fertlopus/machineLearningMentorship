from datetime import date
from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class Address(BaseModel):
    street: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address


person = Person(first_name="aa", last_name="bb", gender=Gender.MALE,
                birthdate="1991-01-01", interests=["travelling", "photo", "football"],
                address = {
                    "street" : "Test street",
                    "postal_code": "Test postal code",
                    "city": "Test city",
                    "country": "Test country"
                })

# print(person)
person_dict = person.model_dump()
print(person_dict["first_name"])
