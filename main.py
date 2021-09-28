import discord
import datetime
import time
import asyncio
import random
import re
import math
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('At')

trainer = ChatterBotCorpusTrainer(chatbot)

conversation = False

client = discord.Client()
@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    global conversation
    if conversation and str(message.author.id) != "886317112367390760":
        response = chatbot.get_response(message.content)
        await message.channel.send(response)
    if message.content == "activate conversation and milk tea" and conversation == False:
        conversation = True
        await message.channel.send("Ok, just wait a little while my consciousness is loading please!")
        trainer.train("chatterbot.corpus.english")
        trainer.train("chatterbot.corpus.english.conversations")
        await message.channel.send("Activated conversation! :tea:")
    if message.content == "die please" and str(message.author.id) == "774498932696547329":
        await message.channel.send("As you wish master :skull:")
        exit()

client.run("ODg2MzE3MTEyMzY3MzkwNzYw.YTz1Ig.-7YhRdyzSkTFG4GSBdx66FxZlYc", bot = True)
