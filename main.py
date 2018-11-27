# -*- coding: utf-8 -*-

# if it doesn't work (encoding error) : wirte " chcp 65001 " in the console

import tweepy
from tweepy import OAuthHandler

import codecs
import json

import pdb

import auth_id

import time

from markold.markold import Markold 

auth = OAuthHandler(auth_id.consumer_key, auth_id.consumer_secret)
auth.set_access_token(auth_id.access_token, auth_id.access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

name = 'EmmanuelMacron'
other = api.get_user(name)

output_name = 'data_' + name + '.txt'
data = []

text = []

nb_pages = 5

to_output = True

tweets_cursor = tweepy.Cursor(api.user_timeline, id=name, tweet_mode='extended').pages(nb_pages)
retry_count = 0
page_count = 0
while True:
    try:
        page = tweets_cursor.next()
        page_count += 1
        print(f'Processing page {page_count}')
        for tweet in page:
            if 'RT @' not in tweet.full_text:
                text.append(tweet.full_text)

    except tweepy.TweepError as err:
        pdb.set_trace()
        print(f"Error code: {err.api_code} with message: {err.message[0]['message']}")
        retry_count += 1
        time.sleep(5)
        if retry_count > 100:
            break

    # We reached the end of the pages
    except StopIteration:
        break  

if to_output:
    with open(output_name, 'w', encoding='utf8')as of:
        for tweet in text:
            of.write(tweet + '\n')

mark = Markold()
markov = 4
to_output = False
to_print = True
mark.import_sentences(text)
sentence = mark.generate_multiple_sentences(markov, 1, to_output=to_output, to_print=to_print)
while len(sentence[0]) > 280:
        sentence = mark.generate_multiple_sentences(markov, 1, to_output=to_output, to_print=to_print)
        
ok_or_not = input()

while ok_or_not != 'y':
    sentence = mark.generate_multiple_sentences(markov, 1, to_output=to_output, to_print=to_print)
    while len(sentence[0]) > 280:
        sentence = mark.generate_multiple_sentences(markov, 1, to_output=to_output, to_print=to_print)

    ok_or_not = input()

api.update_status(sentence[0])