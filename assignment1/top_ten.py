import sys
import json
import operator

hashtag_count = {}

# This is different than tweet_sentiment in that I am only storing the text
def loadTweets(fp):
    for line in fp:
        tweet = json.loads(line)
        # clean data before
        if tweet.get('entities'):
            if tweet.get('entities').get('hashtags'):
                hashtags = tweet.get('entities').get('hashtags')
                for i in range(len(hashtags)):
                    hashtag = hashtags[i].get('text').encode('utf-8')
                    if hashtag not in hashtag_count:
                        hashtag_count[hashtag] = 0
                    hashtag_count[hashtag] += 1

def main():
    tweet_file = open(sys.argv[1])
    loadTweets(tweet_file)
    sorted_count = sorted(hashtag_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        format = "%s %f" % (sorted_count[i][0], float(sorted_count[i][1]))
        print format

if __name__ == '__main__':
    main()