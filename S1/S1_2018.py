N = int(input()) # Number of villages
v = [] # village sizes

# getting village positions
for i in range(N):
    t = float(input())
    v.append(t)
    
#Ordering village positions from least to greatest
v.sort()

size = 1000000000.0 # Max size of a village in case there are no smaller ones

for i in range(0, N):
    if i == N - 1 or i == 0:
        continue
    left = (v[i] + v[i-1]) / 2
    right = (v[i] + v[i+1]) / 2
    if right - left < size:
        size = right - left

print(size)
    

    


