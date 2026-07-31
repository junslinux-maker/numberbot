import os
import json
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

IMAGE_PATH = "assets/image.png"

# 이미지 전송 기준 숫자
IMAGE_TRIGGER = 6000

CHANNEL_FILE = "config/channel.json"


def get_channel_id():
    try:
        with open(CHANNEL_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return int(data.get("channel_id", 0))
    except Exception:
        return 0


def set_channel_id(channel_id: int):
    with open(CHANNEL_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {"channel_id": channel_id},
            f,
            indent=4
        )