from pydantic import BaseModel

class Blog(BaseModel):
    id: int = None
    title: str
    content: str
    category: str
    tags: str