import hikari
import tanchi
import tanjun


component = tanjun.Component()


@component.with_slash_command
@tanchi.as_slash_command("quote", default_to_ephemeral=True)
async def quote(ctx: tanjun.abc.Context) -> None:
    """Retrives a random quote from the database"""
    embed = hikari.Embed(
        title="Quote", description="This command is not implemented yet!"
    )
    await ctx.respond(embed)


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
