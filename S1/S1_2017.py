N = int(input()) # number of games
swifts = input().split() # number of runs per day for swifts
sem = input().split() # number of runs per day for semaphores

count = 0
sum_swifts = 0
sum_sem = 0

# Pretty simple logic
for i in range(N):
    sum_swifts += int(swifts[i])
    sum_sem += int(sem[i])
    if sum_swifts == sum_sem:
        count = i + 1

print(count)



