import discord
from discord.ext import commands

from config.settings import (
    get_channel_id,
    START_NUMBER,
    END_NUMBER,
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

        # 특정 채널만 허용
        if message.channel.id != get_channel_id:
            return

        text = message.content.strip()

        # 숫자가 아니면 무시
        if not text.isdigit():
            return

        number = int(text)

        # 범위 밖이면 무시
        if number < START_NUMBER or number >= END_NUMBER:
            return

        next_number = number + 1

        # 다음 숫자 전송
        await message.channel.send(str(next_number))

        # 6000이면 이미지도 전송
        if next_number == END_NUMBER:
            try:
                await message.channel.send(
                    file=discord.File(IMAGE_PATH)
                )
            except Exception as e:
                print(f"이미지 전송 실패: {e}")


async def setup(bot):
    await bot.add_cog(Counter(bot))