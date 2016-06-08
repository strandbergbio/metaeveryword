# Words from https://github.com/dwyl/english-words

import tokens
import tweepy
import random
import pickle

class TwitterAPI:
    def __init__(self):
        consumer_key = tokens.consumer_key
        consumer_secret = tokens.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = tokens.access_token
        access_token_secret = tokens.access_token_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

def getRandomWord():
    words = pickle.load(open("/home/adam/Desktop/MetaEveryWord/words.p", "rb"))
    word = random.choice(words)
    words.remove(word)
    pickle.dump(words, open("/home/adam/Desktop/MetaEveryWord/words.p", "wb"))
    return "meta" + word
    
if __name__ == "__main__":
    twitter = TwitterAPI()
    foo = getRandomWord()
    twitter.tweet(foo)


