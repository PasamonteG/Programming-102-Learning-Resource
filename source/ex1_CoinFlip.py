import random

def coin_flip():
    toss = random.randint(0,1) # This has taken some Duckduck Go search.
    if toss == 0:
        print('face')
    else:
        print('reverse')

# I'll run the function several times to see randomness of the results.
# I use a for loop to run it many times
for i in range(10):
    coin_flip()
