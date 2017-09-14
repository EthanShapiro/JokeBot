import csv
from core.joke import StoredJoke

_CSV_PATH = 'jokes.csv'
fieldnames = ['rating', 'title', 'joke', 'author', 'post_id']


def save_data(rating, title, joke, author, post_id):
    joke = process_joke(joke)
    joke_data = dict(zip(fieldnames, [rating, title, joke, author, post_id]))
    with open(_CSV_PATH, 'a', newline='', encoding='utf-8-sig') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(joke_data)


# Data Pre-processing
def retrieve_jokes():
    # Use utf-8-sig encoding to remove special characters
    with open(_CSV_PATH, 'r', newline='', encoding='utf-8-sig') as csvfile:
        joke_data = csv.DictReader(csvfile)
        return convert_data_jokes(joke_data)


# remove trailing \r and whitespace
def process_joke(joke):
    joke = joke.replace('\r', '')
    return joke.strip()


def convert_data_jokes(data):
    saved_jokes = []
    for row in data:
        saved_jokes.append(StoredJoke(*[row[name] for name in fieldnames]))
    return saved_jokes
