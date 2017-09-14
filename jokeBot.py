from core import jokeManager
from core import dataManager


def wait_for_input():
    while True:
        response = input("Would you like to hear a joke? (yes or shutdown)")
        if response.lower() == 'yes':
            return True
        elif response.lower() == 'shutdown':
            return False
        else:
            print("I'm sorry, I didn't understand that. Please try again")
            continue


def get_rating():
    while True:
        rating = input("What would you rate this joke out of 10?")
        if not rating.isdigit():
            print("Please enter a number 1-10")
            continue
        elif int(rating) not in range(10+1):
            print("That number is not 1-10, please only numbers 1-10!")
            continue
        else:
            return rating

def show_joke(joke):
    print(str(joke))


while wait_for_input():
    # Get a joke
    joke = jokeManager.get_joke()

    # Show the joke
    show_joke(joke)

    # Get a rating from the user to see which jokes they like the most
    rating = get_rating()

    # Save the joke for data analysis
    dataManager.save_data(rating=rating, title=joke.title, joke=joke.joke, author=joke.author, post_id=joke.post_id)

