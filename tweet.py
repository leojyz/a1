import math

# Use these constants in place of int and string literals to make your code
# easier to read, and less error prone.
# Note that we are using a shorter tweet length to make testing easier.
MAX_TWEET_LENGTH = 50
HASH = '#'

# Add your own constants here, as needed
same = "Same length"
tweet1 = "Tweet 1"
tweet2 = "Tweet 2"

def contains_owly_url(tweet):
    """ (str) -> bool

    Return True if and only if tweet contains a link to an ow.ly URL of the
    form 'http://ow.ly/'.

    Assume tweet is a valid tweet.

    >>> contains_owly_url('Cook receives award: http://ow.ly/WXJFN')
    True
    >>> contains_owly_url('http://ow.ly/VGpA9 Team to transform U of T campus')
    True
    >>> contains_owly_url('Fairgrieve to play in goal http://www.nhl.com')
    False
    """

    # Complete this function body.
    tweet = tweet.split()
    for word in tweet:
        if word.startswith('http://ow.ly/'):
            return True
    return False

# Now define the other functions described in the handout.


def is_valid_tweet(tweet):
#count space
    return len(tweet) < MAX_TWEET_LENGTH and len(tweet) > 0


def add_hashtag(tweet, hashtag):
    tweet_message = tweet + ' #' + hashtag
    if is_valid_tweet(tweet_message):
        return tweet_message
    return tweet


def contains_hashtag(tweet, hashtag):
    tweet = tweet.split()
    for word in tweet:
        if word == hashtag:
            return True
    return False


def report_longest(tweet1, tweet2):
    if len(tweet1) > len(tweet2):
        return tweet1
    elif len(tweet2) > len(tweet1):
        return tweet2
    else:
        return same


def num_tweets_required(message):
    return math.ceil(len(message)/MAX_TWEET_LENGTH)


def get_nth_tweet(message, nth):
    num_of_tweet = num_tweets_required(message)
    if num_of_tweet < nth:
        return ''
    elif num_of_tweet == nth:
        return message[(nth - 1) * MAX_TWEET_LENGTH:]
    else:
        return message[(nth - 1) * MAX_TWEET_LENGTH: nth * MAX_TWEET_LENGTH]
