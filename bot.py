from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer

from datetime import *

# Will be used to train the bot and give the best match

bot = ChatBot(name = "LoPoBot", read_only = True, logic = ['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
greet = ['hello', 'hi', 'how are you?', 'pretty fine'] # Making a small corpus
d1 = ['your name', 'LoPo Bot']
d2 = ['am I good', 'yes you are no doubt']

train = ListTrainer(bot)

for item in  (greet, d1, d2):
  train.train(item)

# Take Commands
command = input('~~~~~~')
bot_response = bot.get_response(command)
print(bot_response)
