from pydantic import BaseModel


class UserProfile(BaseModel):
    nickname: str
    location: str | None = None
    subscription_marketing_newsletter: bool = True


user = UserProfile(nickname="FooBar")
print(user)
