import os


def convert_to_bool(envvar_input):
    return envvar_input.lower() == 'true'


# Organize feature flags that guard features (routes). See app.py
IMAGE_RECEIVER_ENABLED = convert_to_bool(
    os.getenv("IMAGE_RECEIVER_ENABLED", 'False'))
