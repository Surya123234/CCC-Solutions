# Sort the list of tides
# Since each high tide > each low tide, the right half are the high tides and the left half are the low tides
# If there are an odd number of tides, there is 1 more low tide than high tide
# print each low tide in decreasing order and high tide in increasing order alternatingly

import math

N = int(input())
tides = input().split()

for i in range(len(tides)):
    tides[i] = int(tides[i])
tides.sort()

if N % 2 == 0:
    x = N//2
else:
    x = math.ceil(N/2)

low = tides[:x]
high = tides[x:]

low.reverse()

if N % 2 == 0:
    for i in range(x):
        print(low[i], high[i], end = " ")
else:
    for i in range(x-1):
        print(low[i], high[i], end = " ")
    
    print(low[-1])