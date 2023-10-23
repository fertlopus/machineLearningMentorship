from pydantic import BaseModel, EmailStr, model_validator, ValidationError


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @model_validator(mode="before")
    def password_mathc(cls, values):
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password != password_confirmation:
            raise ValueError("Passwords do not match.")
        return values


# validation (case: do not match)
try:
    UserRegistration(email="aaa@google.com", password="aa", password_confirmation="aa")
except ValidationError as e:
    print(str(e))

# validation (case: match)
try:
    test = UserRegistration(email="aaa@google.com", password="aa", password_confirmation="aa")
except ValidationError as e:
    print(str(e))


print(test)
