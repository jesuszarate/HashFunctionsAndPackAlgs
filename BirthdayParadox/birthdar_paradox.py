import random

n = 4000
start = 1
bdays = {}
k = 0
m = 300

def randTrials(start, end, k):
    while 1:
        v = random.randint(start, n)
        if v in bdays:
            return k
            break

        bdays[v] = True
        k += 1

for i in range(1, 300):
    #bdays = {}
    print str(i/300.0) + "\t" + str(randTrials(start, n, k))