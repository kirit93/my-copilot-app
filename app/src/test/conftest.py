import pytest
from fastapi.testclient import TestClient
import os
from importlib import reload
from app import app

try:
    from .temp_env_var import TEMP_ENV_VARS, ENV_VARS_TO_SUSPEND
except ImportError:
    TEMP_ENV_VARS = {}
    ENV_VARS_TO_SUSPEND = []


@pytest.fixture(scope="module")
def test_app():

    client = TestClient(app)
    yield client  # testing happens here


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    monkeypatch.setenv('X-NEON-TOKEN', 'hello')
    monkeypatch.setenv('CLIENT-ID', 'WORLD')
    monkeypatch.setenv("YOUTUBE_TRANSCRIBER_ENABLED", "True")
    os.environ['YOUTUBE_TRANSCRIBER_ENABLED'] = 'True'


@pytest.fixture()
def client():
    app = reload(app)
    yield TestClient(app=app)


@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)
    for env_var in ENV_VARS_TO_SUSPEND:
        os.environ.pop(env_var, default=None)

    yield
    # Will be executed after the last test
    os.environ.clear()
    os.environ.update(old_environ)
