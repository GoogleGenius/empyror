import crescent

plugin = crescent.Plugin("empyror.plugins.internal")


@plugin.include
@crescent.command
async def ping(ctx: crescent.Context, ws: bool = True) -> None:
    """Replies with bot latency"""
    if ws:
        await ctx.respond(f"Pong! `{ctx.app.heartbeat_latency * 1000:.0f}ms`")
    else:
        await ctx.respond("Well, too lazy to check for REST latency so...")
