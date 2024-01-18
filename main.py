import discord
import os
 
TOKEN = os.environ.get('DISCORD_TOKEN')

class MyClient(discord.Client): 
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("http://x.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[13:])

        if message.content.startswith("https://x.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[14:])

        if message.content.startswith("http://twitter.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[19:])

        if message.content.startswith("https://twitter.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[20:])

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
