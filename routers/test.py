from auth.jwt_bearer import jwtBearer
from auth.jwt_handler import signJWT
from fastapi import APIRouter, Body, Depends
from models.model import PostSchema, UserLoginSchema, UserSchema

posts: list[PostSchema] = [
    {"id": 1, "title": "pengiuns", "text": "dfjsofij"},
    {"id": 2, "title": "tigers", "text": "djsoajfdosijofids"},
    {"id": 3, "title": "loalas", "text": "dskjafdjoafijsd"},
]

users: list = [{"email": "Aya@example.com", "password": "Aya123"}]

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
@test.get("/posts/{id}", dependencies=[Depends(jwtBearer())], tags=["posts"])
def get_one_post(id: int):
    if id > len(posts):
        return {"error": "Post with this ID does not exist!"}
    for post in posts:
        if post["id"] == id:
            return {"data": post}


# 4 Post a blog post [A handler for creating post]
@test.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"info": "Post Added"}


# 5 User Signup [ Create a new user]
@test.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@test.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"error": "Invalid login details!"}
