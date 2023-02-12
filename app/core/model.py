from pydantic import BaseModel


class TokenCreationResponseModel(BaseModel):
    v_token: str

    class Config:
        schema_extra = {
            "example": {
                "vToken": "..."
            },
            "headers": {
                "Test": "Boo"
            }
        }
