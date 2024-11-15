n = int(input())
arr =[]

for i in range(n):
    arr.append(input())

for idx, value in enumerate(arr,start=1):
    print(f"{idx}. {value}")