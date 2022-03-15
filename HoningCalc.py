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
artenergy = 0
hitslist = []
success = False

for i in range(times):
    while not success:
        hits += 1

        actualchance = chance + (ech * fails)
        if random.random() < actualchance or artenergy >= 100: #If honing success, move on
            success = True

        else: #If honing fail, increment fails
            artenergy += (actualchance * 100) / 2.15
            fails += 1 
    
    #Add success to list and reset
    hitslist.append(hits)
    hits = 0
    fails = 0
    artenergy = 0
    success = False

#Generating numbers to show user
hitslist.sort()

avg = str(statistics.mean(hitslist))
median = str(statistics.median(hitslist))

fq = times // 5
tq = 4 * fq
fifthpt = str(hitslist[fq])
eightypt = str(hitslist[tq])

best = str(hitslist[0])
worst = str(hitslist[-1])

#Show user statistics
print("Expect between " + fifthpt + " to " + eightypt + " honing attempts per item, " + avg + " on average.")
print()
print("Hits mean: " + avg)
print("Hits median: " + median)
print("Top 20% luck: " + fifthpt)
print("Bottom 80% luck: " + eightypt)
print("Best: " + best)
print("Worst: " + worst)