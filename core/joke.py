class Joke(object):

    def __init__(self, title, joke, author, post_id):
        self.title = title
        self.joke = joke
        self.post_id = post_id
        self.author = author

    def __str__(self):
        return '{0}\n{1}\n{2}\n{3}'.format(self.title, self.joke, self.author, self.post_id)

class StoredJoke(Joke):

    def __init__(self, rating, title, joke, author, post_id):
        self.rating = rating
        self.title = title
        self.joke = joke
        self.post_id = post_id
        self.author = author

    def __str__(self):
        return '{0}/10\n{1}\n{2}\n{3}\n{4}'.format(self.rating, self.title, self.joke, self.post_id, self.author)