import sys
import json
import re

tweet_data = {}
sentiment_data = {}
new_terms = {}


def loadSentiments(fp):
    for sentiment in fp.readlines():
        sent, score = sentiment.strip().split("\t")
        sentiment_data[sent] = float(score)


def loadTweets(fp):
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        # find the tweet sentiment
        score = 0
        if tweet.get('text'):
            ttext = tweet.get('text').encode('utf-8').split()
            for i in range(len(ttext)):
                if ttext[i] in sentiment_data:
                    score += sentiment_data[ttext[i]]
                else:
                    if ttext[i] not in new_terms:
                        new_terms[ttext[i]] = 0
                    new_terms[ttext[i]] += score


def printNewTerms():
    for key in new_terms:
        format = "%s %f" % (key, float(new_terms[key]))
        print format


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadSentiments(sent_file)
    loadTweets(tweet_file)
    printNewTerms()

if __name__ == '__main__':
    main()
