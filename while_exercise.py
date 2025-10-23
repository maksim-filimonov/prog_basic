import random
def g(treshold):
    rn = random.random()
    result = ''
    while rn < treshold:
        result += '-'
        rn = random.random()
    return result
treshold = 0.5
print(g(treshold))