from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostBase(PostBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True
