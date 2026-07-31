import discord
from discord.ext import commands

from config.settings import set_channel_id


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="numberbot")
    @commands.has_permissions(administrator=True)
    async def numberbot(self, ctx, action=None, channel_id=None):

        if action == "setchannel":

            if channel_id is None:
                await ctx.send(
                    "❌ 채널 ID를 입력하세요.\n"
                    "예: !numberbot setchannel 123456789"
                )
                return

            try:
                channel_id = int(channel_id)

                set_channel_id(channel_id)

                channel = self.bot.get_channel(channel_id)

                if channel:
                    await ctx.send(
                        f"✅ 숫자 채널 설정 완료: {channel.mention}"
                    )
                else:
                    await ctx.send(
                        f"✅ 채널 ID {channel_id} 저장 완료"
                    )

            except ValueError:
                await ctx.send("❌ 올바른 채널 ID가 아닙니다.")


async def setup(bot):
    await bot.add_cog(Admin(bot))