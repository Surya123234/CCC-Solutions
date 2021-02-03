total = int(input()) # total amount of numbers in the list

# inputting all the numbers into the list
nums = []
for i in range(total):
    nums.append(int(input()))

#       Algorithm Explanation
# making a new list to store the new numbers
# if the number is > 0, then it is valid, so it is appended into the new list
# if the number is 0, the latest added number is popped (removed) from the new list
# when done iterating through the original list, the new list will only contain the valid numbers
new_nums = []
for i in range(len(nums)):
    if nums[i] > 0:
        new_nums.append(nums[i])
    else:
        new_nums.pop()

# getting the sum of all elements in the list and outputting it
sum = 0
for num in new_nums:
    sum += num

print(sum)