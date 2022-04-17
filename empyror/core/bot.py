# import aiosqlite

from pathlib import Path

import hikari
import tanjun

import empyror


def build_bot() -> hikari.GatewayBot:
    """Build the bot from `hikari.GatewayBot` and call `make_client()`

    Returns
    -------
    bot : hikari.GatewayBot
        The bot created by `hikari.GatewayBot`
    """
    bot = hikari.GatewayBot(empyror.TOKEN)
    make_client(bot)

    return bot


def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    """Create the Tanjun client from `hikari.GatewayBot`

    Parameters
    ----------
    bot : hikari.GatewayBot
        The bot to use for the client

    Returns
    -------
    client : tanjun.Client
        The Tanjun client created from the bot
    """
    client = tanjun.Client.from_gateway_bot(
        bot, declare_global_commands=empyror.GUILD_ID
    )

    client.load_modules(*empyror.get_modules(Path("empyror/modules")))

    return client
