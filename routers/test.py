from fastapi import APIRouter
from models.model import PostSchema

posts: list[PostSchema] = [
    {"id": 1, "title": "pengiuns", "text": "dfjsofij"},
    {"id": 2, "title": "tigers", "text": "djsoajfdosijofids"},
    {"id": 3, "title": "loalas", "text": "dskjafdjoafijsd"},
]
users: list = []

test = APIRouter()


# Get - for testing
@test.get("/", tags=["test"])
def greet():
    return {"hello": "world"}


# Get Posts
@test.get("/post", tags=["posts"])
def get_post():
    return {"data": posts}


# 3 Get single post {id}
@test.get("/posts/{id}", tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {"error": "Post with this ID does not exist!"}
    for post in posts:
        if post["id"] == id:
            return {"data": post}


# 4 Post a blog post [A handler for creating post]
@test.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "Post Added"}
