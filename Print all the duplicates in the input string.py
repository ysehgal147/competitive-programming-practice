# Print all the duplicates in the input string
# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
# Algorithm: Let input string be “geeksforgeeks”
# 1: Construct character count array from the input string.

# count[‘e’] = 4
# count[‘g’] = 2
# count[‘k’] = 2
# ……

# 2: Print all the indexes from the constructed array which have value greater than 1.

string = input()
dict={}
for character in string:
    if character not in dict:
        dict[character] = 1
    else:
        dict[character] += 1

for element in dict:
    if dict[element]>1:
        print(element, dict[element])


