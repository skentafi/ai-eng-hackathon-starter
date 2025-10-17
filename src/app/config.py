import os
import toml
from pathlib import Path

config_path = Path(__file__).resolve().parent.parent.parent / "config.toml"
config = toml.load(config_path)

APP_NAME = config["app"]["name"]
APP_VERSION = config["app"]["version"]
DEBUG_MODE = config["app"]["debug"]

LOGIC_VARIANT = os.getenv("LOGIC_VARIANT", config["estimator"]["logic_variant"])
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", config["estimator"]["currency"])
S3_BUCKET = os.getenv("S3_BUCKET", config["estimator"]["s3_bucket"])