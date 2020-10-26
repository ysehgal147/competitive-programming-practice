# Kadane's Algorithm

x = input()
for _ in range(int(x)):
    length = int(input())
    array = list(map(int,input().split()))
    
    maximum = array[0]
    current = array[0]
    
    for i in array[1:]:
        current = max( i , current + i )
        maximum = max( current, maximum)
        
    print(maximum)