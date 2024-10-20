from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False


class ProdConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="PROD_")


class DevConfig(GlobalConfig):
    model_config = SettingsConfigDict(env_prefix="DEV_")


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True

    model_config = SettingsConfigDict(env_prefix="TEST_")


# metemos el get_config en cache, no es necesario, pero
# quiero saber como puedo hacer lo
@lru_cache()
def get_config(env_state: str):
    config_map = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}

    if not env_state:
        raise ValueError("ENV_STATE is not set. ")

    try:
        return config_map[env_state]()
    except KeyError:
        raise ValueError(
            f"Invalid ENV_STATE '{env_state}'. Expected one of {list(config_map.keys())}"
        )


config = get_config(BaseConfig().ENV_STATE)
