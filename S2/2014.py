N = int(input())

partners = {} 
partners2 = {}
valid = True

# Returns a list of each name separated
line1 = input().split()
line2 = input().split()

for i in range(N):
    partners[line1[i]] = line2[i]  # key is line1 name, value is line2 name
    partners2[line2[i]] = line1[i] # key is line2 name, value is line1 name
    
    #ensuring the ith name on each line is not the same
    if line1[i] == line2[i]:
        valid = False
        break

#checking if the partners match on both lines
if valid:
    for name in partners:
        if partners[name] != partners2[name]:
            valid = False
            break

if valid:
    print("good")
else:
    print("bad")






