import hikari
import tanchi
import tanjun


component = tanjun.Component()


@component.with_slash_command
@tanchi.as_slash_command(default_to_ephemeral=True)
async def ping(
    ctx: tanjun.abc.Context,
    bot: hikari.GatewayBot = tanjun.inject(type=hikari.GatewayBot),
) -> None:
    """Responds with bot latency"""
    embed = hikari.Embed(
        title="Ping",
        description=f"Pong! `{round(bot.heartbeat_latency * 1000)}ms`",
    )
    await ctx.respond(embed)


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
