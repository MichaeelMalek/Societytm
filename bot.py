import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix = '.')
load_dotenv(os.path.join(os.getcwd(), '.env'))
TOKEN = os.getenv("TOKEN")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'ID = {bot.user.id}')
   

bot.run(TOKEN)