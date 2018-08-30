from random import randint
from markovbot import MarkovBot
import os

bot = MarkovBot()

book = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'realdonaldtrump.txt')

# Make your bot read the text!
bot.read(book)

# Choose how many tweets you want to generate
tweets_to_generate = 150

for x in range(0, tweets_to_generate):
    # len of the new tweets that will be generated, in words
    tweet_len = randint(10, 25)
    # generating tweet, based on its len and seedwords!
    tweet = bot.generate_text(tweet_len, seedword=[])

    # writting to our generated sentences to the file the poster will use later
    sentences_list = open("generated_sentences.txt", "a")
    sentences_list.write(tweet + "\n")
    sentences_list.close()
