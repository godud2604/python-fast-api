from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    desc: str
    tags: List[str]
    location: str
    
    class Config:
        schema_extra = {
            "example": {
                "title": "FashAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "desc": "We will your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
