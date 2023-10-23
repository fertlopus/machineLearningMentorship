import time
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class Model(BaseModel):
    d: datetime = datetime.now()


# o1 = Model()
# print(o1.d)
#
# time.sleep(1)
#
# o2 = Model()
# print(o2.d)
#
# print(o1.d < o2.d)

class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: int | None = Field(None, ge=1, le=120)


try:
    Person(first_name="AAA", last_name="BBB", age=30)
except ValidationError as e:
    print(str(e))


try:
    Person(first_name="AAA", last_name="BBB", age=1200)
except ValidationError as e:
    print(str(e))

