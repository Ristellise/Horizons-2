import time
import logging
def printf(*args, speed=None):
    try:
        intspeed = int(speed)
        if speed is not None:
            for x in args:

                print(x, end='')
                time.sleep(intspeed)
        else:
            print(args)
    except ValueError:
        logging.fatal('fatal error! cannot Int speed: ' + speed)