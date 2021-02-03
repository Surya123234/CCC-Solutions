
ana = input() # orginal string
ana2 = input() # new string which could have '*'



# populating dict for original string where keys = chars and values = total times they appear
ana_dic = {}
for letter in ana:
    if letter in ana_dic:
        ana_dic[letter] += 1
    else:
        ana_dic[letter] = 1

# populating dict for new string where keys = chars and values = total times they appear
ana2_dic = {}
for letter in ana2:
    if letter in ana2_dic:
        ana2_dic[letter] += 1
    else:
        ana2_dic[letter] = 1

#           Algorithm Explanation
# Traverse through the keys in the dict for the second string
# The '*' key and its value can be ignored since it is not needed for any calculation
# It is not an anagram if:
# The keys in the new string are NOT present in the original string
# Or if the value for the key in the new string are > than the value for the same key in the original string
# If those 2 conditions are not true, then it IS an anagram

valid = True
for key in ana2_dic:
    if key != '*':
        if key not in ana_dic or ana_dic[key] < ana2_dic[key]:
            valid = False
            break

if valid:
    print("A")
else:
    print("N")