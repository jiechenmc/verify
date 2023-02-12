from pydantic import BaseModel, Field
from fastapi import Header


class TokenCreationResponseModel(BaseModel):
    vToken: str = Field(title="Generated vToken")

    class Config:
        schema_extra = {
            "example": {
                "vToken": "..."
            },
        }


class VerifyOut(BaseModel):

    class Config:
        schema_extra = {
            "example": "null",
        }