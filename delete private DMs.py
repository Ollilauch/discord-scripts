import discord

client = discord.Client()
token = "<your discord token here>"

whitelist = [
    # discord Channel ids you don't want to leave/delete
    4319814918943,
    4123894014211,
]


@client.event
async def on_ready():
    for channel in client.private_channels:
        try:
            if channel.id not in whitelist:
                await channel.close()
        except Exception as e:
            print(e)

client.run(token)
