import yaml
import os
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# config parameters
# Заменяем плейсхолдер telegram_token значением из переменной окружения
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN", config_yaml["telegram_token"])
if telegram_token.startswith("${"):
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables or is invalid")

openai_api_key = os.getenv("OPENAI_API_KEY", config_yaml["openai_api_key"])
if openai_api_key.startswith("${"):
    raise ValueError("OPENAI_API_KEY is not set in environment variables or is invalid")

openai_api_base = config_yaml.get("openai_api_base", None)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
image_size = config_yaml.get("image_size", "512x512")
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)

# читаем переменную окружения от Render
mongodb_uri = os.environ.get('MONGODB_URI')
if mongodb_uri is None:
    raise ValueError("MONGODB_URI is not set in environment variables")

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
