import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json
import pdb
import html

#todo: env variables
auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])

auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])

api = tweepy.API(auth)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

#todo: better class name
class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        json_load = json.loads(data)
        user = json_load['user']['id']
        texts = html.unescape(json_load['text'])
        #insert numerical user ID as an integer in place of insert_user_id
        if user == insert_user_id:
            api = API(auth_handler=auth)
            api.update_status(status=texts)

    def on_error(self, status_code):
        if status_code == 420:
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth, listener=myStreamListener)
#insert numerical user ID as a string in place of insert_user_id
myStream.filter(follow = ['insert_user_id'])

