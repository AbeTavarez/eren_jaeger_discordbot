import random
import json
import requests
import discord
import os
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()

words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encoragements = ["Cheer Up!",
                         "Hang in there", "You are a great person / bot!"]


def get_quote():  # Fetch data from api and parse it
    res = requests.get("http://zenquotes.io/api/random")
    json_data = json.loads(res.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return(quote)


# * Events

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

    if any(word in msg.content for word in words):
        await msg.channel.send(random.choice(starter_encoragements))


client.run(os.getenv('TOKEN'))
