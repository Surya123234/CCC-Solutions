N = int(input())
flowers = []

# making a 2d list with the input, where each sublist is a flower's growth
for i in range(N):
    flowers.append(input().split())

# Each flower grows higher each time, the lowest height for the smallest flower can  exist in any corner of the list
smallest = min(int(flowers[0][0]), int(flowers[0][N-1]), int(flowers[N-1][0]), int(flowers[N-1][N-1]))

'''
zip() produces a tuple by taking the ith element from each argument (or sublist) and making a tuple from it
Eg: [ [1,2,3], [4,5,6], [7,8,9] ]  ->   [ (1,4,7), (2,5,8), (3,6,9) ]
'''

# Rotating the list by 90 degrees counter clockwise until the smallest flower height is at [0][0]
while int(flowers[0][0]) != smallest:
    flowers = list(reversed(list(zip(*flowers))))

# printing out the original flower heights
for i in range(N):
    for j in range(N):
        print(flowers[i][j], end = ' ')
    print()

