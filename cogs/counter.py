import discord
from discord.ext import commands

from config.settings import (
    get_channel_id,
    IMAGE_TRIGGER,
    IMAGE_PATH
)


class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        # 봇 메시지 무시
        if message.author.bot:
            return

        # 설정된 채널만 작동
        if message.channel.id != get_channel_id():
            return

        text = message.content.strip()

        # 숫자만 처리
        if not text.isdigit():
            return

        number = int(text)

        # 1 미만 무시
        if number < 1:
            return

        next_number = number + 1

        # 숫자 출력
        await message.channel.send(str(next_number))

        # 6000이면 이미지 전송
        if next_number == IMAGE_TRIGGER:
            try:
                await message.channel.send(
                    file=discord.File(IMAGE_PATH)
                )
            except Exception as e:
                print(f"이미지 전송 실패: {e}")


async def setup(bot):
    await bot.add_cog(Counter(bot))