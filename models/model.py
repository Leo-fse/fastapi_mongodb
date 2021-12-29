from pydantic import BaseModel, EmailStr, Field


class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "some title about animals",
                "content": "some content about animals",
            }
        }


class UserSchema(BaseModel):
    fullname: str = Field(defalt=None)
    email: EmailStr = Field(defalt=None)
    password: str = Field(defall=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Bek",
                "email": "help@bekbrace.com",
                "password": "123",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(defalt=None)
    password: str = Field(defall=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email": "help@bekbrace.com",
                "password": "123",
            }
        }
