import sys

n = int(input())

arr1 =[]
for i in range(n):
    arr1.append(input())

arr2 = list(set(arr1))
arr2.sort()
arr2.sort(key=len)

for i in arr2:
    print(i)