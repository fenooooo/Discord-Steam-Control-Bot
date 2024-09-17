
# Discord Steam Control Bot

This bot allows users to control various aspects of their Steam account via Discord commands. It can change your Steam nickname, launch/close games, manage downloads, and more.

## Features

- Change your Steam nickname
- Launch or close a game by its Steam App ID
- Start or pause downloads for games
- List your owned games on Steam

## Setup

1. Clone the repository.
2. Install dependencies:

   ```
   pip install discord.py python-dotenv steam
   ```

3. Create a `.env` file and add your Discord bot token and Steam API credentials:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   STEAM_API_KEY=your_steam_api_key
   STEAM_ID=your_steam_id
   COMMAND_PREFIX=!
   ```

4. Run the bot:

   ```
   python bot.py
   ```

## Commands

- `!changenick <new_nickname>`: Change your Steam nickname.
- `!launchgame <app_id>`: Launch a game by its Steam App ID.
- `!closegame <app_id>`: Close a game by its Steam App ID.
- `!startdownload <app_id>`: Start downloading a game by its App ID.
- `!pausedownload <app_id>`: Pause the download for a game by its App ID.
- `!listgames`: List all owned Steam games along with their App IDs.

## Requirements

- Python 3.6 or higher
- discord.py
- python-dotenv
- Steam API Key
