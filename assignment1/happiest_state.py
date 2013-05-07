import sys
import json

state_scores = {}
sentiment_data = {}


def loadSentiments(fp):
    for sentiment in fp.readlines():
        sent, score = sentiment.strip().split("\t")
        sentiment_data[sent] = float(score)


def loadTweets(fp):
    for line in fp:
        tweet = json.loads(line)
        score = 0
        if tweet.get('place'):
            if tweet.get('place').get('country_code') == 'US':
                fname = tweet.get('place').get('full_name').split()
                state = fname[len(fname) - 1]
                if tweet.get('text'):
                    ttext = tweet.get('text').encode('utf-8').split()
                    for i in range(len(ttext)):
                        if ttext[i] in sentiment_data:
                            score += score + sentiment_data[ttext[i]]
                if state not in state_scores:
                    state_scores[state] = 0
                state_scores[state] += score


def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    loadSentiments(sentiment_file)
    loadTweets(tweet_file)

    # find the state with the largest score
    v = list(state_scores.values())
    k = list(state_scores.keys())
    print k[v.index(max(v))]

if __name__ == '__main__':
    main()
