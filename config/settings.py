import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Token
TOKEN = os.getenv("TOKEN")

# 허용할 채널 ID
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))

# 6000일 때 보낼 이미지
IMAGE_PATH = "assets/image.png"

# 시작 번호
START_NUMBER = 5098

# 마지막 번호
END_NUMBER = 6000