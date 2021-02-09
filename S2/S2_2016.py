question = int(input()) # 1 = min total speed, 2 = max total speed
N = int(input()) # total citizens in each country

# input
Dcit = input().split()
Pcit = input().split()

# turning each element to an integer
for i in range(N):
    Dcit[i] = int(Dcit[i])
    Pcit[i] = int(Pcit[i])

#sorting
Dcit.sort()
Pcit.sort()

speed = 0

# max(a,b) is added to the total speed
# for min speed, compare the fastest from Dcity to the fastest in Pity for each element
# for max speed, compare the fastest in a city to slowest in the other city for each element

if question == 2:
    Dcit.reverse()

for i in range(N):
    speed += max(Dcit[i], Pcit[i])

print(speed)