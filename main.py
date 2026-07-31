import asyncio
import discord
from discord.ext import commands

from config.settings import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)


@bot.event
async def on_ready():
    print("=" * 50)
    print(f"로그인 완료 : {bot.user}")
    print(f"봇 ID      : {bot.user.id}")
    print("=" * 50)


async def load_extensions():
    await bot.load_extension("cogs.counter")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())