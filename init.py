import praw
import tweepy

#Change client id and client secret!
reddit = praw.Reddit(client_id='d5F-aZ-nf6C08Q',
					 client_secret='yM5xi3gH92zrs8r35iKxmz6zsnI',
					 user_agent='my user agent')

api_key = 'Mdzv5TYgJhVhCMIDoFNjG1q7d'
api_secret_key = '3cwTkKahKLK2wKkFuPYeaoUQBWG3Hmc4k7vLI06C629twr8bNH'
access_token = '801190254506082310-DRUdsOz16zOVKV9WTzU2NUkwLu6lCuT'
access_token_secret = 's8XsZ2T87vY3Uw6sH0762pk1dUPDyAW2jxjSq2633g7ev'

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)