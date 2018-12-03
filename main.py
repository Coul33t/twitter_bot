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

import argparse

def parse_args():
    """ Arguments parser. """

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--at", help="the person to imitate", type=str)
    parser.add_argument("-n", "--noat", help="ignore replies to people (tweets starting with @someone)", action='store_true')
    parser.add_argument("-p", "--pages", help="the number of page to gather", type=int, default=5)
    parser.add_argument("-m", "--markov", help="the number of words to look forward for (more = more realistic sentences, but less variation from original sentences)",
                        type=int, default=3)
    parser.add_argument("-o", "--output", help="the name of the output file", type=str)
    args = parser.parse_args()

    if not 0 < int(args.markov):
        parser.error("Error: markov value must be > 0.")

    if not args.at:
        parser.error("Error: must specify a twitter account (without the @).")

    return args

def main(args):
    auth = OAuthHandler(auth_id.consumer_key, auth_id.consumer_secret)
    auth.set_access_token(auth_id.access_token, auth_id.access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    name = args.at

    output_name = 'data_' + name + '.txt'

    text = []

    tweets_cursor = tweepy.Cursor(api.user_timeline, id=name, tweet_mode='extended').pages(args.pages)
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
                    if args.noat and tweet.full_text[0] != '@':
                        text.append(tweet.full_text)

        except tweepy.TweepError as err:
            retry = True
            pdb.set_trace()
            print(f"Error code: {err.response.text} with message: ")
            retry_count += 1
            print(f'Retrying in 1s (total retries = {retry_count})')
            time.sleep(1)
            if retry_count > 100:
                break

        # We reached the end of the pages
        except StopIteration:
            break  

    if args.output:
        with open(output_name, 'w', encoding='utf8')as of:
            for tweet in text:
                of.write(tweet + '\n')

    mark = Markold()
    to_output = False
    to_print = True
    mark.import_sentences(text)
    sentence = mark.generate_multiple_sentences(args.markov, 1, to_output=to_output, to_print=to_print)
    while len(sentence[0]) > 280:
            sentence = mark.generate_multiple_sentences(args.markov, 1, to_output=to_output, to_print=to_print)

    ok_or_not = input()

    while ok_or_not != 'y':
        if ok_or_not == 'q':
            return
        sentence = mark.generate_multiple_sentences(args.markov, 1, to_output=to_output, to_print=to_print)
        while len(sentence[0]) > 280:
            sentence = mark.generate_multiple_sentences(args.markov, 1, to_output=to_output, to_print=to_print)

        ok_or_not = input()

    api.update_status(sentence[0])

    print('Tweeted!')

    time.sleep(1)
    tweet_id = api.user_timeline(id = api.me().id, count = 1)[0].id
    api.update_status('(Tweet like ' + name +')', tweet_id) 

if __name__ == '__main__':
    args = parse_args()

    main(args)