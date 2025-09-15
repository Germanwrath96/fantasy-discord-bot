import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    send_fantasy_update.start()

@tasks.loop(minutes=30)
async def send_fantasy_update():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("🏈 Fantasy update: Trevor Lawrence threw for 274 yards and 2 TDs!")

bot.run(TOKEN)
