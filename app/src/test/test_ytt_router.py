from fastapi.testclient import TestClient
import os

from app import app
from models.http_request_models import *
from models.http_response_models import *
from models.youtube_transcriber import *


def test_post_video_successfully(env_setup, test_app):
    payload = {"video_id": "93eLj7wPhYI"}
    response = test_app.post("/ytt/video",
                             json=payload,
                             headers={
                                 "X-NEON-TOKEN": "hello",
                                 "CLIENT-ID": "WORLD"
                             })
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["status"] == "Healthy"
    assert response_json["message"] == "Transcription processed successfully."
    assert len(response_json["content"]["transcript"]) > 0
    assert response_json["content"]["transcript"][0] == {
        "text": "[Music]",
        "start": 1.97,
        "duration": 10.64
    }

def test_post_video_unauthenticated(test_app):
    payload = {"video_id": "93eLj7wPhYI"}
    
    response = test_app.post("/ytt/video",
                             json=payload,
                             headers={
                                 "X-NEON-TOKEN": "bad",
                                 "CLIENT-ID": "auth"
                             })
    response_json = response.json()

    assert response.status_code == 400
    # assert response_json["status"] == "Healthy"
    # assert response_json["message"] == "Transcription processed successfully."
    # assert len(response_json["content"]["transcript"]) > 0
    # assert response_json["content"]["transcript"][0] == {
    #     "text": "[Music]",
    #     "start": 1.97,
    #     "duration": 10.64
    # }
