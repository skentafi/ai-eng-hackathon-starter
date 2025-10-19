import os
import toml
from pathlib import Path

# Load config.toml from project root
config_path = Path(__file__).resolve().parent.parent.parent / "config.toml"
config = toml.load(config_path)

# App metadata
APP_NAME = config.get("app", {}).get("name", "Cost Estimator")
APP_VERSION = config.get("app", {}).get("version", "0.1.0")
DEBUG_MODE = config.get("app", {}).get("debug", False)

# Estimator settings with env override
LOGIC_VARIANT = os.getenv("LOGIC_VARIANT", config.get("estimator", {}).get("logic_variant", "default-logic"))
DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", config.get("estimator", {}).get("currency", "USD"))
S3_BUCKET = os.getenv("S3_BUCKET", config.get("estimator", {}).get("s3_bucket", "default-bucket"))


def get_config():
    """
    Optional helper to expose config as a dictionary.
    """
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "debug": DEBUG_MODE,
        "logic_variant": LOGIC_VARIANT,
        "currency": DEFAULT_CURRENCY,
        "s3_bucket": S3_BUCKET
    }
