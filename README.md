# Eren Jaeger Discord Bot 🤖

## Getting Started

### Prerequisites

- Python
- Discord.py
- Request
- DotEnv
- OS
- Random
- JSON

### Bot Discord Commands

`$new` :
`$new my new quote` - creates new quote

### Runing the program

1. Fork repo.

2. Open it in your favorite code editor.

3. Create a `.env` file and copy and paste the following:

`export TOKEN="paste_your_bot_token_here"`

then copy your bot's token from your discord app

finally paste it inside the quotes of the `TOKEN` variable.

4. If you are uploding your code online using git, create a `.gitignore` file then type `.env` inside the gitignore file

then run `git init`.

4. From the project's directory, run the following code in your terminal:

```
python3 eren_jaeger_bot.py
```

5- If everything was successful you should see `We have logged in as <discord_bot_name>` printed to the console.

### Sample Code

```
# Adds new quote to db

    if msg.content.startswith("$new"):
        new_quote = msg.content.split("$new ", 1)[1]
        update_quote_list(new_quote)
        await msg.channel.send("New quote added!")
```
