#Subarray with 0 sum

counter = int(input())
for _ in range(counter):
    length = int(input())
    array = list(map(int, input().split()))

    hashmap = []
    summed = 0
    result = "No"

    for i in array:
        summed += i

        if summed == 0 or summed in hashmap:
            result = "Yes"
            break
        else:
            hashmap.append(summed)

    if result != "Yes":
        print("No")
    else:
        print("Yes")
