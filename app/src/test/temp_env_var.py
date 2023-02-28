# Inspired by https://shay-palachy.medium.com/temp-environment-variables-for-pytest-7253230bd777
TEMP_ENV_VARS = {
    'X-NEON-TOKEN': 'hello',
    'CLIENT-ID': 'WORLD',
    'YOUTUBE_TRANSCRIBER_ENABLED': 'True',
}

ENV_VARS_TO_SUSPEND = [
    'DATABRICKS_TOKEN',
]
