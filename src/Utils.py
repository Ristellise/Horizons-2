import random
import traceback
def panic():
    """
    Panic Routine used to crash the game if it is unintended.
    :return: Nothing 
    """
    print("Horizons 2 Has encoundered a Serious Error and must shutdown!")
    print("-------------------------------------------------------------------------")
    traceback.print_stack()
    print("-------------------------------------------------------------------------")
    import sys
    sys.exit("Horizons 2 Paniced.")
def cat():
    _rand = random.randint(0,5)
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