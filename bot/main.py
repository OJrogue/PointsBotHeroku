import discord
import os
import server
import discord
import functions

TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print("Logged in as: {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_split = message.content.lower().split(" ")
    if message_split[0] == "points":

        name = message_split[1].replace("_"," ")


        points = ft.read_points(name)

        if points:
            embedVar = discord.Embed(title=points[0],description=points[1],color=0x3498db)
            embedVar.add_field(name="Points", value=points[2], inline=False)
            embedVar.add_field(name="Armor", value=points[3], inline=True)
            embedVar.add_field(name="Weapons", value=points[4], inline=True)
            embedVar.add_field(name="Echoes", value=points[5], inline=True)

            await message.channel.send(embed=embedVar)

        else:
            await message.channel.send("Toon not found")


server.server()
bot.run(TOKEN)
