low = int(input())
high = int(input())

count = 0

#very few cool numbers exist in a certain range
#Since input nums can be 10^8 max, find the largest num so that n^6 is within the range (being 21)
#loop through that and check for cool nums
for i in range(1, 22):
    if low <= i**6 <= high:
        count += 1

print(count)