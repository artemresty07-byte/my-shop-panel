import discord
import os
from flask import Flask
from threading import Thread

# Создаем мини-сервер, чтобы Render не отключал бота
app = Flask('')
@app.route('/')
def home():
    return "I'm alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.change_presence(activity=discord.Game(name="Build & Scripts | Shop"))

# Запуск
keep_alive()
token = os.environ.get("DISCORD_TOKEN")
client = MyBot(intents=discord.Intents.default())
client.run(token)

