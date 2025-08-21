from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_PATH: Path = Path(__file__).parent.parent.parent.resolve()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        frozen=True,
    )

    data_path: Path = PROJECT_PATH / 'data'