import discord as d
import numpy as np 
import pandas as pd
import os

client = d.Client()

df = pd.read_csv('The_Quotes_Doc_-_Quotes.csv')
print(df.loc[1,'Quote'])
print(os.getenv('HOME'))

@client.event
async def on_message(message):
	if message.content.startswith('!quote'):
		try :
			index = int(message.content.split()[1]) - 1
			print(df.loc[index])
			name = df.loc[index, 'Quote']
			print(name)
			exp = df.loc[index, 'Explanation']
			msg = "Quote # " + str(index + 1) + " " + name + ": " + exp
			print(message)
			await message.channel.send(msg)
		except :
			await message.channel.send("OOPSIES you made a fucky wucky, no quote exists uwu")

client.run(os.getenv('TOKEN'))