import os
from os.path import join, dirname
from dotenv import load_dotenv
"""
Load the settings from the .env file
"""

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")