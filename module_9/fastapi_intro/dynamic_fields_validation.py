from datetime import date, datetime
import time
from pydantic import BaseModel, Field, ValidationError


def list_factory():
    return ["a", "b", "c"]


class Model(BaseModel):
    l: list[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: list[str] = Field(default_factory=list)


o1 = Model()
print(o1.d)

time.sleep(1)

o2 = Model()
print(o2.d)

print(o1.d < o2.d)
