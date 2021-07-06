import random
from datetime import datetime

def exp():
    ls = []
    for _ in range(5000000):
        ls.append(random.randint(1, 10**20))


    hash = set(ls)
    start = datetime.now()
    for _ in range(100):
        random.randint(1, 10**20) in hash
    print('1. 100 раз поискал в списке за ' + str((datetime.now() - start).total_seconds()) + ' секунд')
exp()
