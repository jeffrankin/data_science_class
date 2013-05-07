import sys
import json

tweet_terms = {}
total_terms = 0

def loadTweets(fp):
    global total_terms
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        if tweet.get('text'):
            ttext = tweet.get('text').encode('utf-8').split()
            for i in range(len(ttext)):
                total_terms += 1
                if ttext[i] not in tweet_terms:
                    tweet_terms[ttext[i]] = 0
                tweet_terms[ttext[i]] += 1

def main():
    tweet_file = open(sys.argv[1])
    loadTweets(tweet_file)
    for key in tweet_terms:
        format = "%s %f" % (key, tweet_terms[key] / float(total_terms))
        print format

if __name__ == '__main__':
    main()
