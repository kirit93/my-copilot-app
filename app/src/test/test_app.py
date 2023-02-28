from routers.router_utils import *
from datetime import datetime
import time
import os
from fastapi.testclient import TestClient

from settings import Settings
from feature_flags import *
from metadata_tags import METADATA_TAGS
from models.http_response_models import *
from app import app

# Home page here


def test_get_healthcheck(test_app):
    response = test_app.get("/")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["status"] == "Healthy"
    assert response_json["message"] == "Healthcheck looks good. Content is purposely blank."


def test_get_healthcheck(test_app):
    response = test_app.get("/info")
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["status"] == "Healthy"
    assert response_json["message"] == "Info looks good."
    assert response_json["content"] == {
        "app_name": "Neon Money Club Fast API Starter Kit",
        "environment": os.environ.get("environment")
    }
