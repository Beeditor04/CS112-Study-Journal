n = int(input())
arr = [int(i) for i in input().split()]

minIndex = 0
for i in range(n):
    minIndex = i if arr[i] < arr[minIndex] else minIndex

product = 1
for i in range(n):
    product *= arr[i] if i != minIndex else (arr[i] + 1)

print(product) 


