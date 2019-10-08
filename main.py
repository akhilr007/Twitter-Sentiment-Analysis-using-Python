from textblob import TextBlob
import tweepy
import sys
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part) / float(whole)


consumerKey = "czygU0sYHnDHpvktQWWwfZK6f"
consumerSecret = "ZIvS9wifWeteEYvvwPEHuPKPDA2hxT5ZHSpaJF4t7IHnd6feCJ"
accessToken = "1021675329063026688-RrNt0mqIrysaK1DIFHVCBtSVqpeBfb"
accessTokenSecret = "JQRybcI3YCjBDNuMh9DRztOFBLd8zFamvgnwpjyaz6AiX"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter keyword or hashtag to search about: ")
numberOfSearchTerms = int(input("Enter how many tweets to analyse: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(numberOfSearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if(analysis.sentiment.polarity  == 0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0):
        negative += 1
    elif(analysis.sentiment.polarity > 0):
        positive += 1

positive = percentage(positive, numberOfSearchTerms)
negative = percentage(negative, numberOfSearchTerms)
neutral = percentage(neutral, numberOfSearchTerms)
polarity = percentage(polarity, numberOfSearchTerms)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')


print("How people are reacting on " + searchTerm + " by analyzing " + str(numberOfSearchTerms) + " Tweets.")

if(polarity == 0.00):
    print("Neutral")
elif(polarity > 0.00):
    print("positive")
elif(polarity < 0.00):
    print("Negative")

labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['blue', 'yellow', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on " + searchTerm + " by analyzing " + str(numberOfSearchTerms) + " Tweets.")
plt.axis("equal")
plt.tight_layout()
plt.show()






