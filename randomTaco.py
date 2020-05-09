import pullData as pd
import random


def randomNumber(number):
    return random.randint(0,number)

def randomShell():
    data = pd.getShells()
    num = randomNumber(len(data)-1)
    print(data[num])


