# A Program to check if strings are rotations of each other or not

#     1. Create a temp string and store concatenation of str1 to
#        str1 in temp.
#        temp = str1.str1

#     2. If str2 is a substring of temp then str1 and str2 are 
#        rotations of each other.

#     Example:                 
#                      str1 = "ABACD"
#                      str2 = "CDABA"

#      temp = str1.str1 = "ABACDABACD"
#      Since str2 is a substring of temp, str1 and str2 are 
#      rotations of each other.

string1 = input() # Initialized string
string2 = input() # To be checked

connectstring = string1 + string1

if string2 in connectstring:
    print(1)
else:
    print(0)