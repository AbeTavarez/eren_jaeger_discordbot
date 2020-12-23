import json
import requests
import discord
import os
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()


def get_quote():
    res = requests.get("http://zenquotes.io/api/random")
    json_data = json.loads(res.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return(quote)


@client.event  # @event: as soon as the bot is ready
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event  # @event: when a message is received
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$tatakae'):
        quote = get_quote()
        await msg.channel.send(quote)


client.run(os.getenv('TOKEN'))
