from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Anime Style Backend",
    version="0.0.1",
    contact={
        "name": f"Justin Wong",
        "url": "https://anime.style",
        "email": "justinryanwong@berkeley.edu"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get('/')
def redirect_to_docs():
    return RedirectResponse('/docs')



# from routers.router_utils import *
# from datetime import datetime
# import time
# from fastapi import FastAPI, Depends
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.exception_handlers import (
#     http_exception_handler,
#     request_validation_exception_handler,
# )
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import RedirectResponse
# from functools import lru_cache
# from dotenv import load_dotenv
# import os

# from settings import Settings
# from feature_flags import *
# from metadata_tags import METADATA_TAGS
# from models.http_response_models import *

# load_dotenv()  # load .env file
# app = FastAPI(
#     title="Anime Style Backend",
#     version="0.0.1",
#     contact={
#         "name": f"Justin Wong",
#         "url": "https://anime.style",
#         "email": "justinryanwong@berkeley.edu"
#     },
#     openapi_tags=METADATA_TAGS,
#     license_info={
#         "name": "Apache 2.0",
#         "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
#     },
# )


# @lru_cache()
# def get_settings():
#     return Settings()


# # CORS middleware
# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)

# # Home page here


# @app.get('/')
# def redirect_to_docs():
#     return RedirectResponse('/docs')


# @app.get("/healthcheck", response_model=Response, tags=["healthcheck"])
# def healthcheck():
#     return Response(
#         status="Healthy",
#         message="Healthcheck looks good. Content is purposely blank."
#     )


# @app.get("/info", response_model=InfoResponse, tags=["info"])
# async def info(settings: Settings = Depends(get_settings)):
#     return InfoResponse(
#         status="Healthy",
#         message="Info looks good.",
#         content=InfoContent(app_name=settings.app_name,
#                             environment=settings.environment
#                             )
#     )

# ########### Add Flag guarded Features here ###########

# if IMAGE_RECEIVER_ENABLED:
#     from routers.image_receiver_router import *
#     app.include_router(imageReceiverRouter,
#                        prefix="/image-receiver",
#                        tags=["image-receiver"],
#                        dependencies=[
#                            Depends(get_token_headers),
#                            Depends(get_settings)
#                        ],
#                        responses={404: {"description": "Not found"}})

# # TODO:
# # 1. Referral code handling
# # 2. Payments?
# # 3. Push notifications (https://firebase.flutter.dev/docs/messaging/notifications/)

# ########### End of Flag Guarded Features    ###########
