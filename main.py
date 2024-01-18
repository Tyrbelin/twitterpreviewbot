import discord
import os
from flask import Flask

app = Flask(__name__)
@app.route('/health', methods=['GET'])
def health_check():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

TOKEN = os.environ.get(f"DISCORD_TOKEN").strip()
print('token : ' + TOKEN)

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
client = MyClient(intents=intents)
intents.messages = True
client.run(TOKEN)
