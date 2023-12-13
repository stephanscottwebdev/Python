import discord
from discord.utils import get
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Your Discord bot token
TOKEN = 'MTE2NjcyMDc5NzQ3ODUwNjU4OA.GB6eeM.i-4sD2BvzgaU6D9K8v3EhRa_iH4STU54ddXats'

# Initialize the bot
bot = discord.Client(intents=intents)
bot2 = commands.Bot(command_prefix='!', intents=intents)

# List of random names/weapons
names = ["Ash", "Balistic", "Bangalore", "Bloodhound", "Catalyst", "Caustic", "Conduit", "Crypto", "Fuse", "Gibraltar", "Horizon",
		"Lifeline", "Loba", "Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie",
		"Vantage", "Watson", "Wraith"]
weapon = ["30-30", "Havoc", "Flatline", "Hemlock", "R-301", "Nemesis", "Alternator", "R-99", "Volt", "C.A.R.", "Devotion",
        "Spitfire", "Rampage", "G7 Scout", "Triple Take", "Charge Rifle", "Longbow", "Sentinal",
        "EVA-8", "Mastiff", "Mozambique", "Peacekeeper", "P2020", "RE-45", "L-Star"]

# Items in the crafter:
# "Bocek" "Prowler" "Wingman"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    #print(f"Message received: {message.content}")
    user_name = message.author.display_name if message.author.display_name else message.author.name
    if message.content == '!bot':
        await message.channel.send(f'What up, {user_name}!? Here are my commands. Type: !r for a random Champion. !w for random guns. !a for both a random Champion and weapons. !z if you are lazy and need the next 3 Champions chosen for you. !tmb IYKYK.')

    if message.content == '!r':
        #print("Command !r recognized")
        #num_names = 3  # Number of random names to generate
        random_name = random.choice(names)
        await message.channel.send(f'Daaaaang, {user_name} you cute as SHIT! Your random champion is {random_name}. Clap some cheeks baby!')

    if message.content == '!w':
        #print("Command !w recognized")
        num_weapons = 2  # Number of random weapons to generate
        random_weapon = random.sample(weapon, num_weapons)
        await message.channel.send(f'You so bad with that roller movement {user_name}, use a ' + ' and a '.join(random_weapon) + ' to make up for it. You\'ll probably wiff your shots anyway.')

    if message.content == '!a':
        #print("Command !a recognized")
        random_name = random.choice(names)
        num_weapons = 2  # Number of random weapons to generate
        random_weapon = random.sample(weapon, num_weapons)
        await message.channel.send(f'Ok {user_name} you big ol\' cutie! Your champion is {random_name}. Try using a ' + ' and a ' .join(random_weapon) + ' this game! K BYYYYYYYYYYE!!')

    if message.content == '!z':
        #print("Command !a recognized")
        num_names = 3  # Number of random names to generate
        random_name = random.sample(names, num_names)
        await message.channel.send(f'Ok, {user_name} you lazy ass. Here are your next three Champions: ' + ', '.join(random_name) + '. Ya biiiiiiiitch.')  

    if message.content == '!tmb':
        await message.channel.send(f'(⑅˘꒳˘)☞ (‿|‿) ԅ(≖‿≖ԅ)')

    if message.content == '!uWu':
        await message.channel.send(f'🥺 👉👈')

# Start the bot
bot.run(TOKEN)
