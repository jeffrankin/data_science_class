import sys
import json
import re
from datetime import datetime, date, time

tweet_data = []
sentiment_data = {}
term_data = {}
new_terms = {}

# This is different than tweet_sentiment in that I am only storing the text
def loadTweets(fp):
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        if tweet.get('text'):
            tweet_data.append(tweet.get('text').encode('utf-8'))

def loadSentiments(fp):
    for sentiment in fp.readlines():
        sent, score = sentiment.strip().split("\t")
        sentiment_data[sent] = float(score)

# only store tweets that have some kind of sentiment
def loadTweetSentiment(tweet):
    score = 0
    has_score = 0
    for key in sentiment_data:
        keyre = r'\b' + re.escape(key) + r'\b'
        if re.search(keyre, tweet, re.IGNORECASE):
            has_score = 1
            score = score + sentiment_data[key]
        if has_score:
            term_data[tweet] = score

def parseTweetData():
    for key in term_data:
        twit = key.split();
        score = term_data.get(key)
        for i in range(len(twit)):
            term = twit[i].lower()
            if term not in new_terms:
                new_terms[term] = []
            new_terms[term].append(score)


def printNewTerms():
    for key in new_terms:
        sum = 0
        for i in range(len(new_terms[key])):
            sum = sum + new_terms[key][i];
        avg = sum / len(new_terms[key])
        format = "%s %f" % (key, avg)
        # print format

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadSentiments(sent_file)
    loadTweets(tweet_file)
    print datetime.now()
    for i in range(len(tweet_data)):
         loadTweetSentiment(tweet_data[i])
    print datetime.now()
    parseTweetData()
    printNewTerms()

if __name__ == '__main__':
    main()
