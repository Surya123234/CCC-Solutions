J = int(input()) # Number of jerseys
A = int(input()) # Number of athletes

size = []
for i in range(J):
    size.append(input())

# if small, and the pref is that or bigger, satisfied
# if sizes match, satisfied
# if M is pref, then if L exists, match
# if match, change size[n] to done to not iterate through that index
count = 0
for i in range(A):
    line = input().split()    #[0] is size, [1] is num
    n = size[int(line[1]) - 1]
    if n != 'Done':
        if line[0] == 'S' and (n == 'S' or n == 'M' or n == 'L'):
            count += 1
            size[int(line[1]) - 1] = 'Done'
        elif line[0] == 'M' and (n == 'M' or n == 'L'):
            count += 1
            size[int(line[1]) - 1] = 'Done'
        elif line[0] == 'L' and n == 'L':
            count += 1
            size[int(line[1]) - 1] = 'Done'
print(count)
