import os

# import aiosqlite

import hikari
import tanjun

import empyror


def build_bot() -> hikari.GatewayBot:
    bot = hikari.GatewayBot(empyror.TOKEN)
    make_client(bot)

    return bot


def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    client = tanjun.Client.from_gateway_bot(
        bot, declare_global_commands=empyror.GUILD_ID
    )

    client.load_modules(
        *[
            f"empyror.modules.{module[:-3]}"
            for module in os.listdir("./empyror/modules")
            if module.endswith(".py") and not module.startswith("_")
        ]
    )

    return client
