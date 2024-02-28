import tweepy
import os

a = os.getenv("school_consumer_key")
b = os.getenv("school_consumer_secret")
c = os.getenv("school_access_token")
d = os.getenv("school_access_secret")
e = os.getenv("school_bearer")

# pass in twitter API auth keys
client = tweepy.Client(
    bearer_token=e,
    consumer_key = a,
    consumer_secret = b, 
    access_token = c,
    access_token_secret = d
)

async def post(message):
    client.create_tweet(text=message)

''' twitter api too expensive rip

def getLastLink():
    userid = client.get_user(username="")
    print(client.get_list_tweets(id = userid, max_results=1))

'''

# create graphs of views/likes, need full api for that