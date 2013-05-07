import sys
import json
import re

tweet_data = []
sentiment_data = {}

def loadTweets(fp):
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        if tweet.get('text'):
            tweet_data.append(tweet)

def loadSentiments(fp):
    for sentiment in fp.readlines():
        sent, score = sentiment.strip().split("\t")
        sentiment_data[sent] = float(score)

def printTweetSentiment(tweet,i):
    score = 0
    for key in sentiment_data:
        keyre = r'\b' + re.escape(key) + r'\b'
        if re.search(keyre, tweet.encode('utf-8'), re.IGNORECASE):
            # print key
            # print sentiment_data[key]
            score = score + sentiment_data[key]
    tweet_sent = "%f" % (score)
    # tweet_sent = "%f" % (score)
    print tweet_sent

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadSentiments(sent_file)
    loadTweets(tweet_file)
    for i in range(len(tweet_data)):
    # for i in range(10):
        printTweetSentiment(tweet_data[i]['text'],i)

if __name__ == '__main__':
    main()
