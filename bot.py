import os
import discord
#from dotenv import load_dotenv

#load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
#client.run(os.getenv('TOKEN'))
client.run('MTAwNTk0Njk2NTE2MDM4MjQ4NA.G10Evw.saov9d_GDLwiLl1xsbydrjIjoCP2pmWCNVhRqQ')