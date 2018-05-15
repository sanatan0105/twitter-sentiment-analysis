import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'UwHh9p3tf3KPdY0XNHcTysq5Z'
consumer_secret = 'xyBLAu4lLXrR3lYTdvzg1MC3VUDwFSk3mda07hpcLYhvYlbg1i'
access_token = '945067566-mG3UykrUXjBvP0rufpPuXipcuKHThFqk6AnMINeL'
access_token_secret = 'jetvClgbt0tkmc5ueggoV9ZFOmoSS7RU7MxXxmPY4yJAW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text.encode("utf-8"))
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
