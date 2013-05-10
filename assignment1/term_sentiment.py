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

# Using score of the tweet for the basis for new terms
def loadTweetsScore(fp):
    new_terms_this_pass = []
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        # find the tweet sentiment
        score = 0
        if tweet.get('text'):
            new_terms_this_pass = []
            ttext = tweet.get('text').encode('utf-8').split()
            for i in range(len(ttext)):
                if ttext[i] in sentiment_data:
                    score += sentiment_data[ttext[i]]
                else:
                    if ttext[i] not in new_terms:
                        new_terms[ttext[i]] = 0
                        new_terms_this_pass.append(ttext[i])
            for j in range(len(new_terms_this_pass)):
                new_terms[new_terms_this_pass[j]] += score


def loadTweets(fp):
    new_terms_this_pass = []
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        # find the tweet sentiment
        score = 0
        pos_count = 0
        neg_count = 0
        if tweet.get('text'):
            new_terms_this_pass = []
            ttext = tweet.get('text').encode('utf-8').split()
            for i in range(len(ttext)):
                if ttext[i] in sentiment_data:
                    score += sentiment_data[ttext[i]]
                else:
                    if ttext[i] not in new_terms:
                        # print "New Term", ttext[i]
                        counts = {'pcount': 1, 'ncount': 1}
                        new_terms[ttext[i]] = counts
                    new_terms_this_pass.append(ttext[i])
            for j in range(len(new_terms_this_pass)):
                # print "Score", score
                if score > 0:
                    new_terms[new_terms_this_pass[j]]['pcount'] += 1
                else:
                    new_terms[new_terms_this_pass[j]]['ncount'] += 1


def printNewTerms():
    for key in new_terms:
        format = "%s %f" % (key, float(new_terms[key]['pcount']) / float(new_terms[key]['ncount']))
        print format


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadSentiments(sent_file)
    loadTweets(tweet_file)
    printNewTerms()

if __name__ == '__main__':
    main()
