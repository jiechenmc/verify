import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.core.model import VerifyOut
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Header

api_description = \
"""
This service will handle the creation of new verification tokens and verifying users
"""

app = FastAPI(
    title="loqi-verify",
    description=api_description,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get(
    "/verify",
    response_model=VerifyOut,
    description="Match the user against our database",
    responses={
        200: {
            "description":
            "Database match was successful and user role info is cached into cookie/localstorage",
            "headers": {
                'Cache-Control': {
                    "description": "Cache the user's role information locally",
                    "type": "string"
                }
            }
        },
        401: {
            "description": "Failed to authorize with the information provided"
        },
        422: {
            "description": "Invalid JSON request"
        }
    })
async def verify_user(X_UID: str = Header(default=None),
                      X_VTOKEN: str = Header(default=None)):
    return JSONResponse(content="null")


# @app.post("/verify",
#           response_model=TokenCreationResponseModel,
#           description="Creates a new token with permission given to user X",
#           response_description="Success",
#           responses={},
#           )
# async def create_new_verification_token():
#     data = ""
#     return 0