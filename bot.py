
import os
import discord
from discord.ext import commands
import requests
from steam.webapi import WebAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
STEAM_API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

# Set up the bot
bot = commands.Bot(command_prefix=PREFIX)

# Set up the Steam API
api = WebAPI(key=STEAM_API_KEY)

# Change Steam nickname
@bot.command(name='changenick', help="Change your Steam nickname.")
async def change_nickname(ctx, *, new_nick):
    try:
        # Dummy function for changing Steam nickname (API function could vary)
        response = api.call('ISteamUser.SetPersonaName', steamid=STEAM_ID, persona_name=new_nick)
        if response['success'] == 1:
            await ctx.send(f"Successfully changed Steam nickname to {new_nick}")
        else:
            await ctx.send(f"Failed to change nickname.")
    except Exception as e:
        await ctx.send(f"Error occurred: {e}")

# Launch a game by its Steam App ID
@bot.command(name='launchgame', help="Launch a game by its Steam App ID.")
async def launch_game(ctx, app_id):
    try:
        # Dummy endpoint to simulate game launch (actual API control could be different)
        response = api.call('ISteamRemoteClient.StartStreaming', steamid=STEAM_ID, appid=app_id)
        if response.get('success'):
            await ctx.send(f"Launching game with App ID {app_id}.")
        else:
            await ctx.send("Failed to launch game.")
    except Exception as e:
        await ctx.send(f"Error occurred: {e}")

# Close a game by its Steam App ID
@bot.command(name='closegame', help="Close a game by its Steam App ID.")
async def close_game(ctx, app_id):
    try:
        # Dummy endpoint to simulate game closure
        response = api.call('ISteamRemoteClient.StopStreaming', steamid=STEAM_ID, appid=app_id)
        if response.get('success'):
            await ctx.send(f"Closing game with App ID {app_id}.")
        else:
            await ctx.send("Failed to close game.")
    except Exception as e:
        await ctx.send(f"Error occurred: {e}")

# Start downloading a game by its Steam App ID
@bot.command(name='startdownload', help="Start downloading a game by its Steam App ID.")
async def start_download(ctx, app_id):
    try:
        # Simulate starting a game download
        response = api.call('ISteamRemoteStorage.StartFileDownload', steamid=STEAM_ID, appid=app_id)
        if response.get('success'):
            await ctx.send(f"Starting download for game with App ID {app_id}.")
        else:
            await ctx.send("Failed to start download.")
    except Exception as e:
        await ctx.send(f"Error occurred: {e}")

# Pause a download for a game by its Steam App ID
@bot.command(name='pausedownload', help="Pause the download of a game by its Steam App ID.")
async def pause_download(ctx, app_id):
    try:
        # Simulate pausing a game download
        response = api.call('ISteamRemoteStorage.StopFileDownload', steamid=STEAM_ID, appid=app_id)
        if response.get('success'):
            await ctx.send(f"Pausing download for game with App ID {app_id}.")
        else:
            await ctx.send("Failed to pause download.")
    except Exception as e:
        await ctx.send(f"Error occurred: {e}")

# Show the list of owned games
@bot.command(name='listgames', help="Show the list of your owned games.")
async def list_games(ctx):
    try:
        # Retrieve owned games from Steam
        response = api.call('IPlayerService.GetOwnedGames', steamid=STEAM_ID, include_appinfo=True)
        games = response['response']['games']
        game_list = "
".join([f"{game['name']} (App ID: {game['appid']})" for game in games])
        await ctx.send(f"Your Steam games:
{game_list}")
    except Exception as e:
        await ctx.send(f"Error occurred: {e}")

bot.run(TOKEN)
