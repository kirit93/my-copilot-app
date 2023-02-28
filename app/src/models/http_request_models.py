from typing import Union, List
from pydantic import BaseModel
from datetime import datetime

from models.http_request_enums import SupportedStyles


class TextToImageRequest(BaseModel):
    prompt: str

    class Config:
        schema_extra = {
            "example": {
                "prompt": "a photo of an astronaut riding a horse on mars",
            }
        }


class ImageReceiverRequest(BaseModel):
    '''
    Triggers inferencing for the Image Received and the styled desired to generate.
    '''
    user_id: str
    filename: str
    encoded_image: str
    styles: List[SupportedStyles]

    class Config:
        schema_extra = {
            "example": {
                "user_id": "abc123",
                "filename": "abc123_1",
                "encoded_image": "SomeLongBase64EncodedImage",
                "styles": [
                    "one_piece",
                    "my_hero_academy"
                ]
            },
        }
