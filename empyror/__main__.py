import os

from dotenv import load_dotenv

import hikari
import lightbulb


load_dotenv()


token: str = os.environ["TOKEN"]
guild_id: hikari.Snowflake = hikari.Snowflake(os.environ["GUILD_ID"])


def create_bot() -> lightbulb.BotApp:
    bot = lightbulb.BotApp(token=token, default_enabled_guilds=guild_id)
    bot.load_extensions_from("./empyror/extensions")

    return bot


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    create_bot().run()
