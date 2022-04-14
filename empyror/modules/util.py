import hikari
import tanchi
import tanjun


component = tanjun.Component()


@component.with_slash_command
@tanchi.as_slash_command("id", default_to_ephemeral=True)
async def id(ctx: tanjun.abc.Context) -> None:
    """Responds with your user id"""
    embed = hikari.Embed(
        title="Id",
        description=f"User id is: ```{ctx.author.id}```",
    )
    await ctx.respond(embed)


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(component.copy())
