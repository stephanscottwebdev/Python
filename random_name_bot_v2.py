import discord
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Your Discord bot token
TOKEN = ''

# Initialize the bot
bot = discord.Client(intents=intents)

# List of random names
names = ["Ash", "Balistic", "Bangalore", "Bloodhound", "Catalyst", "Caustic", """Conduit",""" "Crypto", "Fuse", "Gibraltar", "Horizon",
		"Lifeline", "Loba", "Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie",
		"Vantage", "Watson", "Wraith"]
weapon = ["Havoc", "Flatline", "Hemlock", "R-301", "Nemesis", "Alternator", """Prowler,""" "R-99", "Volt", "C.A.R.", "Devotion",
        """"L-Star,""" "Spitfire", "Rampage", "G7 Scout", "Triple Take", "30-30", """Bocek",""" "Charge Rifle", "Longbow", "Sentinal",
        "EVA-8", "Mastiff", "Mozambique", "Peacekeeper", "RE-45", "P2020", "Wingman"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    #print(f"Message received: {message.content}")
    if message.author == bot.user:
        return

    if message.content.startswith('!random'):
        #print("Command recognized")
        random_name = random.choice(names)
        await message.channel.send(f'Oh you cute as SHIT, your random champion is {random_name}. Clap some cheeks baby!')

    if message.content.startswith('!weapon'):
        #print("Command recognized")
        random_weapon = random.choice(weapon)
        random_weapon2  = random.choice(weapon)
        await message.channel.send(f'You so bad with that roller movement, use a {random_weapon} and a {random_weapon2} to make up for it. You\'ll probably wiff your shots anyway.')
      
    if message.content.startswith('!touchmybutt'):
        await message.channel.send(f'UwU (⑅˘꒳˘)☞ (‿|‿) ԅ(≖‿≖ԅ)')
 
# Start the bot
bot.run(TOKEN)
