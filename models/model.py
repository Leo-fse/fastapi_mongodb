from pydantic import BaseModel  # , EmailStr, Field


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
