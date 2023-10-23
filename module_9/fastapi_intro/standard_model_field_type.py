from pydantic import BaseModel


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    weight: float

    def __str__(self):
        return (f"Person:\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\n"
                f"age: {self.age}\nweight: {self.weight}")


person = Person(first_name="Foo", last_name="Bar", age=100, weight=100)
print(person)