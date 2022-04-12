import random

import hikari
import lightbulb


fun = lightbulb.Plugin("Fun")


@fun.command
@lightbulb.command("quote", "Returns a random quote from the database")
@lightbulb.implements(lightbulb.SlashCommand)
async def quote(ctx: lightbulb.Context) -> None:
    """Returns a random quote from the (nonexistent) database"""

    quote_list: list[str] = [
        "Quote 1",
        "Quote 2",
        "Quote 3",
    ]

    quote: str = random.choice(quote_list)

    embed = hikari.Embed(
        title="Quote",
        description=quote,
    )

    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fun)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(fun)
