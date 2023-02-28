import json
import re
import base64
import fastapi
import os
from fastapi import APIRouter, HTTPException

from models.http_request_models import *
from models.http_response_models import *

# from google.cloud import storage

imageReceiverRouter = APIRouter()
# storage_client = storage.Client()
BUCKET_NAME = "anime.style"


@imageReceiverRouter.post("/", response_model=ImageReceiverResponse)
async def predict(ImageReceiverRequest: ImageReceiverRequest):
    '''
    Assumes that the Client App will upload images directly to S3 (or GCS) bucket.
    '''
    fp = f"user-uploaded-images/{ImageReceiverRequest.user_id}/{ImageReceiverRequest.filename}"
    # bucket_blob = storage_client.bucket(BUCKET_NAME).blob(fp)
    print(fp, ImageReceiverRequest.encoded_image[:20])

    regex = r"(?<=data:)(.*)(?=;)"
    split = ImageReceiverRequest.encoded_image.split('base64')
    # format_image = re.findall(regex, split[0])[0]
    # base64_image = base64.b64decode(split[1])
    # bucket_blob.upload_from_string(base64_image, content_type=format_image)

    s3_url = "something_url"
    expected_wait_time = estimate_wait_time(len(ImageReceiverRequest.styles))
    # TODO: call model inference endpoint
    return ImageReceiverResponse(
        status="Healthy",
        message=f"Successfully triggered inferencing image at {fp}",
        content=ImageReceiverContent(
            s3_url=s3_url,
            estmated_wait_time_minutes=expected_wait_time
        ),
    )


def estimate_wait_time(n_styles, num_images_to_generate=100):
    '''
    Returns estimated wait time in seconds with the assumptions that inference takes 20 seconds each
    and that we need to generate 100 images. Plus 1 to always round up.
    '''
    ESTIMATED_TIME_PER_INFERENCE = 20  # seconds
    SECONDS_PER_MINUTE = 60
    return ((ESTIMATED_TIME_PER_INFERENCE * num_images_to_generate) // SECONDS_PER_MINUTE) + 1
