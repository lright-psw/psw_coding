n = int(input())

for _ in range(n):
    pw = len(input())
    if pw>=6 and pw<=9:
        print("yes")
    else:
        print("no")
