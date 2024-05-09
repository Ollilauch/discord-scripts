import discord

client = discord.Client()
token = "<your discord token here>"

whitelist = [
    # discord guild ids you don't want to leave
    123456789101112131,
    987654321010203040
]


@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)

client.run(token)
