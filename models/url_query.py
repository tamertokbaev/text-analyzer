from pydantic import BaseModel


class URLQuery(BaseModel):
    url: str
