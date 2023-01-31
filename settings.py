import os
from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()


class BotSettings(BaseSettings):
    bot_token: SecretStr = os.getenv("BOT_TOKEN")


class SiteApiSettings(BaseSettings):
    X_RapidAPI_Key: SecretStr = os.getenv("X_RapidAPI_Key")
    X_RapidAPI_Host: SecretStr = os.getenv("X_RapidAPI_Host")
