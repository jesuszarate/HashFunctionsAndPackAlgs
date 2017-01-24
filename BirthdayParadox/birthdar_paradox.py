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
            bdays[v] = True
            print "\n" + str(v)
            print k
            break
        bdays[v] = True
        k += 1


    print bdays.keys()

for i in range(1, 300):
    randTrials(start, n, k)