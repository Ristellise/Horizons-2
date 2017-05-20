import re
import os
def loadmod(absLocation):
    for root, dirs, files in os.walk(absLocation):
        if files == re.search('\.xlsx',files)