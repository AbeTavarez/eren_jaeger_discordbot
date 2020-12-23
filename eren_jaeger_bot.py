import random
import json
import requests
import discord
import os
from dotenv import load_dotenv
load_dotenv()


client = discord.Client()

db = {}

words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encoragements = ["Cheer Up!",
                         "Hang in there", "You are a great person / bot!"]


def get_quote():  # Fetch data from api and parse it
    res = requests.get("http://zenquotes.io/api/random")
    json_data = json.loads(res.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return(quote)


def update_encouragements(encouraging_msg):  # adds new encourgement
    if "encouragments" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_msg)
        db["encouragements"] = encouragements
    else:
        db["encouragemets"] = [encouraging_msg]


def delete_encouragement(index):  # deletes encouragement
    encouragements = db["encouragemets"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements

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

    options = starter_encoragements
    if "encouragements" in db.keys():
        options = options + db["encouragements"]

    if any(word in msg.content for word in words):
        await msg.channel.send(random.choice(options))

    if msg.content.startswith("$new"):  # adds new message to db
        encouraging_msg = msg.content.split("$new ", 1)[1]
        update_encouragements(encouraging_msg)
        await msg.channel.send("New encouraging message added!")


client.run(os.getenv('TOKEN'))
