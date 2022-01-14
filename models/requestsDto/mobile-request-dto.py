from pydantic.main import BaseModel


class Mobile(BaseModel):
    class Config:
        orm_mode = True

    mobile: str
