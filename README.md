# twitter_bot

A twitter bot that gathers tweets from a person, then generates new sentences from the data.

## Requirements 

* The [Markold](https://github.com/Coul33t/markold) library
* A Twitter developper account
* A file named auth_id, containing the variables `consumer_key`, `consumer_secret`, `access_token` and `access_secret` (all from the twitter developper account)

## Usage
`py gui.py` for the GUI version.

`py main.py` for the CLI version.  
Required parameters :
* `-a` / `--at` : the person's @name (without the @)

Optional parameters :
* `-n` / `--noat` (défault: `false`): ignore tweets that are replies to people (tweets starting with a " @name ")  
* `-p` / `--page` (default: `5`): the number of pages to gather tweets from
* `-m` / `--markov` (default: `3`): the number of word to look forward for. Basically, the higher the value, the more realistic the sentences, at the cost of variation from original sentences. Setting a value of `1` will produce very random sentences
* `-o` / `--output` (default: empty): the name of the local output file. This output is different from the displayed sentence
* `-r` / `--ref` (default: `false`): adds a reference to the original person (with a " @ ")
