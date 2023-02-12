import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.core.model import TokenCreationResponseModel
from fastapi import Response

description = \
"""
This service will handle the creation of new verification tokens and verifying users
"""

app = FastAPI(
    title="loqi-verify",
    description=description,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)


@app.get("/verify",
         response_model=None,
         description="Insert later",
         responses={})
async def verify_user():
    return 0


@app.post("/verify",
          response_model=TokenCreationResponseModel,
          description="Insert later",
          response_description="Success",
          responses={})
async def create_new_verification_token():
    return 0