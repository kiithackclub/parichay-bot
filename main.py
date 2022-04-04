import discord
import os
import json
from dotenv import load_dotenv
from airtable import Airtable
import random

load_dotenv()

intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents = intents)

airtable = Airtable(os.getenv('AIRTABLE_API_KEY'), os.getenv('AIRTABLE_BASE_URL'), "appqLAIXpfmBRorop")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    channel = client.get_channel(800981464828215296)
    member_details = airtable.get_members_by_discord_id(str(member), "tblB9sWiSRn2pVG2E")
    member_details = json.loads(member_details.text)
    notes = ""
    try:
        notes = member_details['records'][0]['fields']['notes']
    except KeyError:
        return

    print(member_details['records'][0]['fields']['notes'])
    # await channel.send(f'{member.mention} says "{notes}"')
    color = [0xa633d6,0x338eda,0x33d6a6,0xff8c37,0x5bc0de]
    embedVar = discord.Embed(title="Welcome Message", description=f'{member.mention} wants to be introduced as:\n"{notes}"', color=random.choice(color))
    embedVar.set_thumbnail(url=member.avatar_url)
    embedVar.set_footer(text='Check the pinned message in <#798945447267926038> for the detailed map of the server!')
    await channel.send(embed=embedVar)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hi'):
        await message.channel.send('Hello!')

client.run(os.getenv('DISCORD_BOT_TOKEN'))
