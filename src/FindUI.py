import os
from src import Gconstants
for file in os.listdir(os.getcwd() + '\Resources\\UI'):
    Gconstants.uifiles.append(os.getcwd() + '\\' + file)