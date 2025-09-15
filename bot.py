import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="./.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# Setup bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Fantasy Bot is now online!")
    else:
        print("❌ Channel not found or invalid ID.")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(DISCORD_TOKEN)
