import discord
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# Your Discord bot token
TOKEN = 'MTE2NjcyMDc5NzQ3ODUwNjU4OA.G4JX4A.3ziv_Im5NVZX0qyZP0cHFbBBbeDw2zKolVTOco'

# Initialize the bot
bot = discord.Client(intents=intents)

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
    if message.author == bot.user:
        return

    #if message_content.startswith('!bot'):
        #await message.channel.send(f'What up baby? Here are my commands. Type: !r for a random Champion. !w for random guns. !a for both a random Champion and weapons! !tmb IYKYK.')

    if message.content.startswith('!r'):
        #print("Command !r recognized")
        random_name = random.choice(names)
        # Get user by id, get username with userid
        #user = bot.get_user(user_id)
        #username = client.get_user(user_id)
        await message.channel.send(f'Oh you cute as SHIT, your random champion is {random_name}. Clap some cheeks baby!')

    if message.content.startswith('!w'):
        #print("Command !w recognized")
        # Get user by id, get username with userid
        #user = bot.get_user(user_id)
        #username = client.get_user(user_id)
        random_weapon = random.choice(weapon)
        random_weapon2  = random.choice(weapon)
        await message.channel.send(f'You so bad with that roller movement, use a {random_weapon} and a {random_weapon2} to make up for it. You\'ll probably wiff your shots anyway.')
    
    if message.content.startswith('!a'):
        #print("Command !a recognized")
        # Get user by id, get username with userid
        #user = bot.get_user(user_id)
        #username = client.get_user(user_id)
        random_name = random.choice(names)
        random_weapon = random.choice(weapon)
        random_weapon2  = random.choice(weapon)
        await message.channel.send(f'Ok cutie! Your champion is {random_name}. Try using a {random_weapon} and a {random_weapon2} this game! K BYYYYYYYYYYE!!')

    if message.content.startswith('!tmb'):
        await message.channel.send(f'UwU (⑅˘꒳˘)☞ (‿|‿) ԅ(≖‿≖ԅ)')
 
# Start the bot
bot.run(TOKEN)
