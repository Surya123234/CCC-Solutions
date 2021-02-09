import math

# checks if a number is prime, only up till sqrt(num), since a factor of x can only exist <= sqrt(x)
# starts at 2 since 0 and 1 are not needed to check for prime numbers
def is_prime(x):
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

# creating a list of input integers

N = int(input())
nums = []

for i in range(N):
    nums.append(int(input()))

# checks if each num in the list is prime by using the formula: 2*num = A + B , where A is j
for i in range(len(nums)):
    for j in range(2, nums[i]):
        if is_prime(j) and is_prime(2*nums[i] - j):
            print(j, 2*nums[i] - j)
            break

