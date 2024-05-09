import discord

client = discord.Client()
token = "<your discord token here>"

whitelist = [
    # discord friend ids you don't want to remove
    13232379844971,
    43124219812911
]


@client.event
async def on_ready():
    for friend in client.friends:
        try:
            if friend.id not in whitelist and friend.type is discord.RelationshipType.friend:
                await friend.delete()
        except Exception as e:
            print(e)

client.run(token)
