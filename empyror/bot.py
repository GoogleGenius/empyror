from __future__ import annotations

__all__: tuple[str, ...] = ("build_bot",)


import crescent

from empyror.config import TOKEN


def build_bot() -> crescent.Bot:
    """Build the instance of crescent.Bot"""
    bot = crescent.Bot(token=TOKEN, banner=None)
    bot.plugins.load("empyror.plugins.internal")

    return bot
