import discord
from discord.utils import get
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Your Discord bot token
TOKEN = 'MTE2NjcyMDc5NzQ3ODUwNjU4OA.GkoEmp.7Ekx79mv2m5okpTKg1UduNcbve8QpNUfurS_3M'

# Initialize the bot
bot = discord.Client(intents=intents)
bot2 = commands.Bot(command_prefix='!', intents=intents)

# List of random names/weapons
names = ["Ash", "Balistic", "Bangalore", "Bloodhound", "Catalyst", "Caustic", "Crypto", "Fuse", "Gibraltar", "Horizon",
		"Lifeline", "Loba", "Maggie", "Mirage", "Newcastle", "Octane", "Pathfinder", "Rampart", "Revenant", "Seer", "Valkyrie",
		"Vantage", "Watson", "Wraith"]
weapon = ["Havoc", "Flatline", "Hemlock", "R-301", "Nemesis", "Alternator", "R-99", "Volt", "C.A.R.", "Devotion",
        "Spitfire", "Rampage", "G7 Scout", "Triple Take", "Charge Rifle", "Longbow", "Sentinal",
        "EVA-8", "Mastiff", "Mozambique", "Peacekeeper", "P2020", "Wingman"]

# Items in the crafter:
#"30-30" "Bocek" "Prowler" "L-Star" "RE-45"
#"Conduit"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    #print(f"Message received: {message.content}")
    user_name = message.author.display_name if message.author.display_name else message.author.name
    if message.content.startswith('!bot'):
        await message.channel.send(f'What up, {user_name}!? Here are my commands. Type: !r for a random Champion. !w for random guns. !a for both a random Champion and weapons. !z if you are lazy and need the next 3 Champions chosen for you. !tmb IYKYK.')

    if message.content.startswith('!r'):
        #print("Command !r recognized")
        random_name = random.choice(names)
        await message.channel.send(f'Daaaaang, {user_name} you cute as SHIT! Your random champion is {random_name}. Clap some cheeks baby!')

    if message.content.startswith('!w'):
        #print("Command !w recognized")
        num_weapons = 2  # Number of random weapons to generate
        random_weapon = random.sample(weapon, num_weapons)
        #random_weapon2  = random.choice(weapon)
        await message.channel.send(f'You so bad with that roller movement {user_name}, use a ' + ' and a '.join(random_weapon) + ' to make up for it. You\'ll probably wiff your shots anyway.')
    
    if message.content.startswith('!a'):
        #print("Command !a recognized")
        random_name = random.choice(names)
        num_weapons = 2  # Number of random weapons to generate
        random_weapon = random.sample(weapon, num_weapons)
        await message.channel.send(f'Ok {user_name} you big ol\' cutie! Your champion is {random_name}. Try using a ' + ' and a ' .join(random_weapon) + ' this game! K BYYYYYYYYYYE!!')

    if message.content.startswith('!z'):
        #print("Command !a recognized")
        num_names = 3  # Number of random names to generate
        random_name = random.sample(names, num_names)
        #random_name = random.choice(names)
        #random_name2 = random.choice(names)
        #random_name3 = random.choice(names)
        await message.channel.send(f'Ok, {user_name} you lazy ass. Here are your next three Champions: ' + ', '.join(random_name) + '. Ya biiiiiiiitch.')  

    if message.content.startswith('!tmb'):
        await message.channel.send(f'UwU (⑅˘꒳˘)☞ (‿|‿) ԅ(≖‿≖ԅ)')
 
# Start the bot
bot.run(TOKEN)
