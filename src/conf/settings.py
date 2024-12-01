import pathlib
import os
from dotenv import load_dotenv

from dotenv import dotenv_values

BASE_DIR = pathlib.Path(__file__).parent.parent.parent
config_path = BASE_DIR / "conf" / "config.yaml"


def get_config():
    load_dotenv()
    config = dict(os.environ)

    config["db_url"] = (
        f"postgresql://{config['DATABASE_USER']}:{config['DATABASE_PASSWORD']}@{config['DATABASE_HOST']}/{config['DATABASE_NAME']}"
    )

    return config


config = get_config()
