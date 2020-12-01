import time

import tweepy
from tweepy import OAuthHandler

from markold.markold import Markold

import auth_id

class TwitterBot:
    def __init__(self):
        self.auth = None
        self.api = None
        self.name= "NO_NAME_PROVIDED"
        self.tweets = []
        self.no_answers = True
        self.pages_to_retrieve = 1
        self.forward_words = 1
        self.nb_tweets_to_generate = 5
        self.output_to_file = False
        self.add_ref = False
        self.generated_tweets = []

    def initialise(self):
        self.auth = OAuthHandler(auth_id.consumer_key, auth_id.consumer_secret)
        self.auth.set_access_token(auth_id.access_token, auth_id.access_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True)

    def gather_tweets(self):
        self.tweets = []

        tweets_cursor = tweepy.Cursor(self.api.user_timeline,
                                      id=self.name,
                                      tweet_mode='extended').pages(self.pages_to_retrieve)

        retry_count = 0
        retry = False
        page_count = 0

        while True:
            try:
                # If we have to retry due to an error, we keep trying for the same page
                if retry:
                    retry = False
                # Else, we take the next page
                else:
                    page = tweets_cursor.next()
                    page_count += 1

                print(f'Processing page {page_count}')
                for tweet in page:
                    if 'RT @' not in tweet.full_text:
                        if self.no_answers and tweet.full_text[0] != '@':
                            self.tweets.append(tweet.full_text)
                        elif not self.no_answers:
                            self.tweets.append(tweet.full_text)

            except tweepy.TweepError as err:
                retry = True
                print(f"Error code: {err.response.text} with message: ")
                retry_count += 1
                print(f'Retrying in 1s (total retries = {retry_count})')
                time.sleep(1)
                if retry_count > 100:
                    break

            # We reached the end of the pages
            except StopIteration:
                break

    def create_new_sentences(self):
        self.generated_tweets = []

        mark = Markold()

        mark.import_sentences(self.tweets)

        for _ in range(self.nb_tweets_to_generate):
            sentence = mark.generate_multiple_sentences(self.forward_words, 1, to_output=self.output_to_file, to_print=False)
            while len(sentence[0]) > 280:
                print('Sentence too big, re-generating a new one')
                sentence = mark.generate_multiple_sentences(self.forward_words, 1, to_output=self.output_to_file, to_print=False)

            self.generated_tweets.append(sentence)

    def tweet_one_sentence(self, idx):
        self.api.update_status(self.generated_tweets[idx])

        print('Tweeted!')

        time.sleep(1)
        tweet_id = self.api.user_timeline(id = self.api.me().id, count = 1)[0].id
        if self.add_ref:
            self.api.update_status('(Tweet like @' + self.name +')', tweet_id)
        else:
            self.api.update_status('(Tweet like ' + self.name +')', tweet_id)

        print('Added reference to original person.')
