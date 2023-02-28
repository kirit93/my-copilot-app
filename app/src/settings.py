from pydantic import BaseSettings


class Settings(BaseSettings):
    # https://fastapi.tiangolo.com/advanced/settings/#the-config-file
    app_name: str = "Neon Money Club Fast API Starter Kit"
    environment: str  # set by environment variables

    class Config:
        env_file = ".env"