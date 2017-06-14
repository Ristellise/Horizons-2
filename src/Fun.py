import random

"""
Module that adds sillyness at every 3.142 seconds 
"""


def cat():
    _rand = random.randint(0, 5)
    if _rand == 1:
        print("Meow!")
    elif _rand == 2:
        print("Who let the Cat out.. AGAIN?!")
    elif _rand == 3:
        print("Kurogari Was here!")
    elif _rand == 4:
        print("Meep!")
    else:
        print("The cat is outta off the bag!")


def birthday(user):
    print("Happy birthday: " + user + " !")


def covfefe():
    print("https://twitter.com/realDonaldTrump/status/869858333477523458")
    print("https://pbs.twimg.com/media/DBJdUgwUQAEFsMG.jpg")
