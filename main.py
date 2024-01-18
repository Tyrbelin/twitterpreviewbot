import discord
import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return '', 200

def run_flask():
    app.run(host='0.0.0.0', port=8080)

TOKEN = os.environ.get("DISCORD_TOKEN")
print('token : ' + TOKEN)

class MyClient(discord.Client): 
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content:
            print(message.content)
        else:
            print("메시지 내용 없음")
            
        if message.content.startswith("http://x.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[13:])

        elif message.content.startswith("https://x.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[14:])

        elif message.content.startswith("http://twitter.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[19:])

        elif message.content.startswith("https://twitter.com/"):
            await message.channel.send('{0.author.mention} https://vxtwitter.com/'.format(message) + message.content[20:])

        await message.delete()

# Run Flask in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Run Discord bot in the main thread
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
