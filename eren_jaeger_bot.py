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

starter_encouragements = ["Cheer Up!",
                          "Hang in there", "You are a great person/bot!"]

if "responding" not in db.keys():
    db["responding"] = True


################ * Helper functions * ######################################

def get_quote():  # Fetch data from api and parse it
    res = requests.get("http://zenquotes.io/api/random")
    json_data = json.loads(res.text)
    quote = json_data[0]['q'] + " -" + json_data[0]["a"]
    return(quote)


def update_encouragements(encouraging_msg):  # adds new encourgement
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_msg)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_msg]


def delete_encouragement(index):  # deletes encouragement
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements

############ * Events * #################################


@client.event  # * @event: As soon as the bot is ready
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event  # * @event: When a message is received
async def on_message(msg):
    if msg.author == client.user:
        return

# Tatakae
    if msg.content.startswith('$tatakae'):
        quote = get_quote()
        await msg.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg.content for word in words):
            await msg.channel.send(random.choice(options))

# * Adds new message to db
    if msg.content.startswith("$new"):
        encouraging_msg = msg.content.split("$new ", 1)[1]
        update_encouragements(encouraging_msg)
        await msg.channel.send("New encouraging message added!")
# * Deletes encoragement
    if msg.content.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.content.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await msg.channel.send(encouragements)

# * Return list of encouragements
    if msg.content.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
            await msg.channel.send(encouragements)

    if msg.content.startswith("$responding"):
        value = msg.content.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await msg.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await msg.channel.send("Responding is off.")


client.run(os.getenv('TOKEN'))
