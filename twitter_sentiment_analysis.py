import tweepy
import sys
from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part,whole):
	return 100*float(part)/float(whole)

consumerKey="jgEdlyavtAbF4oiredqcTFn7g"
consumersecret="Dry1J8sJNzZwOeupvEHi7gHm9aGgAphs6tF4fBnKUOHq3AASSB"
accessToken="1284763185635966976-2bqlCMtgs6wE1lLOSMqvhBZoQ0oAHy"
accessTokenSecret="0139a4CfE9TLldSsf5IdqvpczTxPOL8mVPouhhX3OEniM"


auth=tweepy.OAuthHandler(consumerKey,consumersecret)
auth.set_access_token(accessToken,accessTokenSecret)

api=tweepy.API(auth)

searchkey=input("Enter the keyword:")
num=int(input("Number of tweets you want"))

tweets=tweepy.Cursor(api.search,q=searchkey).items(num)

positive=0
negative=0
nuetral=0
polarity=0
'''for tweet in tweets:
	print(tweet.text)'''

for tweet in tweets:
	analysis=TextBlob(tweet.text)
	#polarity+=analysis.sentiment.polarity
	print(analysis.sentiment.polarity)

	if(analysis.sentiment.polarity==0.00):
		nuetral+=1
	elif(analysis.sentiment.polarity>0.00):
		positive+=1
	elif(analysis.sentiment.polarity<0.00):
		negative+=1

print("Positive tweets="+str(positive))
print("negative tweets="+str(negative))
print("nuetral tweets="+str(nuetral))



