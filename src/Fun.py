import random
import webbrowser
import hashlib

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


def tvtropes():
    webbrowser.open("https://goo.gl/63xysi")


class Antigravity:
    @staticmethod
    def antigravweb():
        webbrowser.open("https://xkcd.com/353/")

    @staticmethod
    def antihash(latitude, longitude, datedow):
        # http://xkcd.com/426/
        h = hashlib.md5(datedow).hexdigest()
        p, q = [('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
        print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))
