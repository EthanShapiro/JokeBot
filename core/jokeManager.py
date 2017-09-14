import praw
from core.joke import Joke
from random import choice


def get_joke_ids_day():
    reddit = praw.Reddit(
                        client_id='ctN1jTBggiKifA',
                        client_secret='dt6assMNm5pMfLM-cmU0dHt5Hcw',
                        user_agent='jokebot')
    # Get top 100 jokes at the time
    return list(reddit.subreddit('jokes').top('day', limit=100))


def convert_ids_to_jokes(ids):
    return [Joke(i.title, i.selftext, i.author, i) for i in ids]


def get_joke():
    joke = choice(jokes)
    jokes.remove(joke)
    return joke


def remove_old_jokes(saved_jokes, jokes):
    """Take stored jokes, and new jokes for today and remove any duplicates"""
    saved_joke_ids = [saved_joke.post_id for saved_joke in saved_jokes]
    joke_ids = [joke.post_id for joke in jokes]
    return [new_id for new_id in joke_ids if new_id not in saved_joke_ids]


joke_ids_today = get_joke_ids_day()
jokes = convert_ids_to_jokes(joke_ids_today)
