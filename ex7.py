import tweepy
from tweepy import OAuthHandler

consumer_key = '03kvkgo1cwRegdODYoiYjAGvU'
consumer_secret = '70AOW5gHXZhKV5mjUVqbh0D9JPdRVzQ9TSR1tJsRRtpuni5THq'
access_token = '815637661281030148-EAIcujr6D32XCTYpabBY9I89AkLN2IW'
access_secret = 'dupx8vxJv3TZ3FBD2OvcEJpt9RRe8YC5p7l4ltUJ1Xfeu'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


id1=raw_input("Please enter tha valid ID of the first user: \t")
id2=raw_input("Please enter tha valid ID of the second user: \t")
id1= id1.strip()
id2= id2.strip()


words1=0
for status in tweepy.Cursor(api.user_timeline,id=id1).items(10):
    for i in range(0,len(status.text.split(" "))):
        words1+=1

words2=0
for status in tweepy.Cursor(api.user_timeline,id=id2).items(10):
    for i in range(0,len(status.text.split(" "))):
        words2+=1


if words1>words2:
    print id1 ,"has more words than", id2, "in their last 10 tweets."
elif words2>words1:
    print id2 ,"has more words than", id1, "in their last 10 tweets."
else :
    print "They both have the same amount of words in their last 10 tweets."
