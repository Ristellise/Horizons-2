import time
import logging
import traceback
import random
import noise
def printf(*args, speed):
    try:
        intspeed = int(speed)
        if speed is not None:
            for arg in args:
                strarg = str(arg)
                for letters in list(strarg):
                    print(letters, end='')
                    time.sleep(intspeed)
        else:
            print(args)
    except (ValueError, TypeError):
        logging.info('Error! cannot Int speed: ' + str(speed))


def Noise(seed, method):
    """

    :param seed: random seed. Leave it empty
    :param method: Simplex/Perlin
    :return: 

    """
    if method == ["Perlin", "perlin"]:
        if seed is 0:
            seed = random.seed()
        print(noise.pnoise2(seed, seed))
    elif method == ["simplex", "Simplex"]:
        if seed is 0:
            seed = random.seed()
        print(noise.snoise2(seed, seed))

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