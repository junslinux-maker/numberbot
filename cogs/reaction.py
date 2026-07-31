import discord
from discord.ext import commands


class Reaction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):

        # 봇 메시지 무시
        if message.author.bot:
            return

        text = message.content.strip()

        # 봇 멘션하면 "뭐"
        if self.bot.user in message.mentions:
            await message.channel.send("뭐")
            return

        # 지정 대사
        if "넌 이제 내 봇이여" in text:
            await message.channel.send("나닛!!")
            return


async def setup(bot):
    await bot.add_cog(Reaction(bot))