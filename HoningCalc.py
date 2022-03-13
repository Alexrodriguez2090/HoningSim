import random, bisect, statistics

#Chance between 1-100
intchance = 0
while intchance <= 0 or intchance > 100:
    intchance = int(input("Base percentage chance of success (1-100): ").strip())

#Change chances to between 0-1
chance = intchance / 100
ech = chance / 10

#Number of times to run simulation
times = 100000

#Initializing variables
hits = 0
fails = 0
hitslist = []
success = False

for i in range(times):
    while not success:
        if random.random() < chance + (ech * fails): #If honing success, move on
            success = True
        else: #If honing fail, increment fails
            fails += 1 
        hits += 1
    
    #Add success to list and reset
    bisect.insort(hitslist, hits)
    hits = 0
    fails = 0
    success = False

#Generating numbers to show user
avg = str(statistics.mean(hitslist))
median = str(statistics.median(hitslist))

fq = times // 4
tq = 3 * fq
quarterpt = str(hitslist[fq])
seventyfivept = str(hitslist[tq])

worst = str(hitslist[-1])
best = str(hitslist[0])

#Show user statistics
print("Expect between " + quarterpt + " to " + seventyfivept + " honing attempts per item, " + avg + " on average.")
print()
print("Hits mean: " + avg)
print("Hits median: " + median)
print("First quartile (25%): " + quarterpt)
print("Third quartile (75%): " + seventyfivept)
print("Best: " + best)
print("Worst: " + worst)