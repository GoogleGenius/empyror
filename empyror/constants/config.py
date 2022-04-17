import os

from dotenv import load_dotenv

import hikari


load_dotenv()


TOKEN: str = os.environ["TOKEN"]
GUILD_ID: hikari.Snowflake = hikari.Snowflake(os.environ["GUILD_ID"])
