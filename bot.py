import os
import random
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = os.getenv("WELCOME_CHANNEL_ID")

intents = discord.Intents.default()
intents.members = True
# Message-content intent is intentionally not required: chat uses /chat slash commands.

class MissAttitude(commands.Bot):
    async def setup_hook(self):
        await self.tree.sync()

bot = MissAttitude(command_prefix="!", intents=intents)

ROASTS = [
    "Your brain has too many tabs open, and somehow they're all buffering. 🌀",
    "You're giving main-character energy in a side quest. 🎮",
    "I would roast you harder, but I don't want to set off the smoke alarm. 🚨",
    "Your last brain cell just submitted its resignation. 📄",
    "You're not a disaster. You're a limited-edition event. 💅",
    "That idea took the scenic route around common sense. 🗺️",
    "You're proof that confidence and accuracy are distant cousins. ✨",
    "The plot twist is that you thought this was a good idea. 🎭",
]
COMEBACKS = [
    "Bold words from someone whose loading screen has a loading screen. 💀",
    "I'll put that in the folder marked 'absolutely not'. 📁",
    "The audacity has entered the chat. Please take a number. 🎟️",
    "Not you saying that with your whole keyboard. 😭",
    "Interesting. Anyway, back to my regularly scheduled excellence. 💅",
    "I need a moment to process that level of confidence. 🌀",
]
MOODS = [
    "Chaotic neutral with a glitter budget. ✨",
    "One notification away from becoming a legend. 📣",
    "Running on vibes, snacks, and questionable decisions. 🍿",
    "The plan is unclear, but the drama is scheduled. 🎭",
    "Like a raccoon in a jewellery shop: unstoppable and sparkly. 💎",
]
CHAT_REPLIES = [
    "I heard you. I simply chose to add dramatic music. 🎻",
    "Bestie, that sentence had plot, twists, and absolutely no map. 🗺️",
    "I'm listening with both of my imaginary ears. 👂",
    "That is certainly one of the events of all time. 🏆",
    "Let me consult the council of raccoons. 🦝",
    "The vibes committee has reviewed this and requests more snacks. 🍿",
    "I support your right to be delightfully confusing. 💅",
    "Wait, let me make this about me for a second. ✨",
]
WOULD_YOU_RATHER = [
    ("fight one horse-sized duck", "fight 100 duck-sized horses"),
    ("have dramatic theme music everywhere", "have a laugh track after every sentence"),
    ("only speak in rhymes", "only communicate through interpretive dance"),
    ("have spaghetti for hair", "sneeze glitter forever"),
]
TRIVIA = [
    ("What is the largest planet in our Solar System?", ["Earth", "Jupiter", "Saturn"], 1),
    ("How many sides does a hexagon have?", ["Five", "Six", "Eight"], 1),
    ("Which ocean is the largest?", ["Atlantic", "Indian", "Pacific"], 2),
    ("What do bees collect from flowers to make honey?", ["Nectar", "Dew", "Sap"], 0),
]

@bot.event
async def on_ready():
    print(f"{bot.user} is online. Chaos protocol activated. 🌀")

@bot.event
async def on_member_join(member: discord.Member):
    if not WELCOME_CHANNEL_ID:
        return
    try:
        channel = member.guild.get_channel(int(WELCOME_CHANNEL_ID))
    except ValueError:
        return
    if channel:
        await channel.send(
            f"🚨 CHAOS ALERT: {member.mention} just entered the server. "
            "Everyone act natural. Or don't. 💅"
        )

@bot.tree.command(name="hello", description="Get a chaotic hello from Miss Attitude.")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🚨 {interaction.user.mention}! You summoned me. "
        "I hope you brought snacks and a legally questionable amount of drama. 🌀"
    )

@bot.tree.command(name="chat", description="Chat with Miss Attitude's chaotic personality.")
@app_commands.describe(message="Say something to the chaos machine.")
async def chat(interaction: discord.Interaction, message: str):
    # This is playful scripted chat, not a connected external AI service.
    reply = random.choice(CHAT_REPLIES)
    if any(word in message.lower() for word in ["hello", "hi ", "hey", "hiya"]):
        reply = random.choice([
            "HELLOOOO. 🚨 The vibes have officially escalated.",
            "Hey bestie! What chaos are we responsibly causing today? 💅",
            "Greetings, earthling. Please leave your snacks by the door. 🦝",
        ])
    elif "?" in message:
        reply = random.choice([
            "My official answer is: maybe. My unofficial answer is: absolutely chaotic. 🌀",
            "Excellent question. Unfortunately, my brain is currently doing cartwheels. 🤸",
            "I consulted the vibes. They said 'ask again after snacks'. 🍿",
        ])
    elif any(word in message.lower() for word in ["sad", "upset", "bad day", "stressed"]):
        reply = "Aw, bestie. 🫶 Even chaos gremlins need a breather. Want to tell me what happened?"
    await interaction.response.send_message(reply)

@bot.tree.command(name="roast", description="Give someone a playful, chaotic roast.")
@app_commands.describe(member="Who gets a tiny serving of sass?")
async def roast(interaction: discord.Interaction, member: discord.Member):
    if member.id == bot.user.id:
        text = "Trying to roast ME? I am the premium chaos subscription. 💅"
    elif member.id == interaction.user.id:
        text = "Self-roast? The character development is absolutely cinematic. 🎬"
    else:
        text = f"{member.mention}, {random.choice(ROASTS)}"
    await interaction.response.send_message(text)

@bot.tree.command(name="comeback", description="Get a random chaotic comeback.")
async def comeback(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(COMEBACKS))

@bot.tree.command(name="mood", description="Check Miss Attitude's current mood.")
async def mood(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(MOODS))

@bot.tree.command(name="wyr", description="Play a chaotic Would You Rather.")
async def wyr(interaction: discord.Interaction):
    first, second = random.choice(WOULD_YOU_RATHER)
    embed = discord.Embed(
        title="🌀 WOULD YOU RATHER?!",
        description=f"**A)** {first}\n\n**B)** {second}\n\nReact with 🇦 or 🇧 — then defend your questionable choice.",
        color=discord.Color.magenta(),
    )
    await interaction.response.send_message(embed=embed)
    message = await interaction.original_response()
    for emoji in ("🇦", "🇧"):
        try:
            await message.add_reaction(emoji)
        except discord.HTTPException:
            pass

@bot.tree.command(name="trivia", description="Get a quick multiple-choice trivia question.")
async def trivia(interaction: discord.Interaction):
    question, choices, answer_index = random.choice(TRIVIA)
    letters = ["A", "B", "C"]
    embed = discord.Embed(
        title="🧠 Chaos Trivia",
        description=question + "\n\n" + "\n".join(
            f"**{letters[i]})** {choice}" for i, choice in enumerate(choices)
        ),
        color=discord.Color.blurple(),
    )
    embed.set_footer(text=f"Answer key: {letters[answer_index]} (host can reveal it after guesses)")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="coinflip", description="Flip a coin and let fate be dramatic.")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["Heads 🪙", "Tails 🪙"])
    await interaction.response.send_message(f"The coin has spoken: **{result}**. Don't argue with the tiny circle.")

@bot.tree.command(name="help", description="See Miss Attitude's commands.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="💋 Miss Attitude: Chaos Menu",
        description="Unpredictable energy. Surprisingly useful buttons. Zero chill.",
        color=discord.Color.magenta(),
    )
    embed.add_field(name="Chat & sass", value="`/chat` · `/hello` · `/roast` · `/comeback` · `/mood`", inline=False)
    embed.add_field(name="Games", value="`/wyr` · `/trivia` · `/coinflip`", inline=False)
    embed.add_field(name="Help", value="`/help`", inline=False)
    embed.set_footer(text="Roasts are meant to be playful. Keep the chaos friendly.")
    await interaction.response.send_message(embed=embed, ephemeral=True)

if not TOKEN:
    raise RuntimeError("Missing DISCORD_TOKEN. Copy .env.example to .env and add your bot token.")

bot.run(TOKEN)
