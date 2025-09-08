import os
import toml
from pathlib import Path

config_path = Path(__file__).parent.parent.parent / "config.toml"
config = toml.load(config_path)

QDRANT_HOST = os.getenv("QDRANT_HOST", config["qdrant"]["host"])
QDRANT_PORT = int(os.getenv("QDRANT_PORT", config["qdrant"]["port"]))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", config["qdrant"]["collection_name"])
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
