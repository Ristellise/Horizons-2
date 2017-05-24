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
    sys.exit("Horizons 2 Panicked.")
