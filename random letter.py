import random

def woordran(woord):
    randomised = ''.join(random.sample(woord, len(woord)))
    print(randomised)

while True:
    original = input("welk woord ")
    woordran(original)
