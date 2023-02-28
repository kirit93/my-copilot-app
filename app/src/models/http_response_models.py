from typing import Union, Any, List
from pydantic import BaseModel
from datetime import datetime


class InfoContent(BaseModel):
    app_name: str
    environment: str

    class Config:
        schema_extra = {
            "example": {
                "app_name": "Fast API Sample.",
                "environment": "dev",
                "settings": {}
            }
        }


class ImageReceiverContent(BaseModel):
    '''
    Content for ImageReceiverResponse.

    This should include the storage url and the expected wait time in minutes.
    '''
    s3_url: str
    estmated_wait_time_minutes: int

    class Config:
        schema_extra = {
            "example": {
                "s3_url": "https://s3.amazon.com",
                "estmated_wait_time": 30
            }
        }


class ResponseContent(BaseModel):
    message: str
    content: Union[dict, None] = None

    class Config:
        schema_extra = {
            "example": {
                "message": "Response content looks good.",
                "content": {
                    "some_key": "some_value"
                }
            }
        }

########################################################################
# Content above this divider
########################################################################


class Response(BaseModel):
    status: str
    time: datetime = datetime.now()
    # add additional content types for returned responses
    content: Union[InfoContent, ImageReceiverContent, None]

    class Config:
        schema_extra = {
            "example": {
                "status": "Healthy",
                "time": "2022-11-17T14:54:56.861324",
                "response": {
                    "message": "Healthcheck looks good. Content is purposely blank.",
                    "content": {
                        "some_key": "some_value"
                    }
                }
            }
        }


class InfoResponse(Response):
    content: InfoContent


class ImageReceiverResponse(Response):
    '''
    Response should indicate an inference run has triggered and returns a ImageReceiverContent.
    '''
    content: ImageReceiverContent

    class Config:
        schema_extra = {
            "example": {
                "status": "Healthy",
                "time": "2022-12-28T22:56:00.165074",
                "message": "Transcription processed successfully.",
                "content": {
                    "s3_url": "https://somebucket.aws.com",
                    "expected_wait_time": 30
                }
            }
        }
