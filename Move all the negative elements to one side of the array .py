# Move all the negative elements to one side of the array

array = list(map(int, input().split()))
negative = []
positive = []
for i in array:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

print(negative+positive)
