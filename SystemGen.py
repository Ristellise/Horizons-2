import random
import math
def GenerateStar():
    mass = random.uniform(0.08, 20)
    basesunmass = int(1.989*(pow(10, 30)))
    starmass = basesunmass*(random.uniform(0.08, 150))
    print(starmass, " ", mass)
    return starmass, mass
for i in range(0, 100):
    GenerateStar()
    i += 1
