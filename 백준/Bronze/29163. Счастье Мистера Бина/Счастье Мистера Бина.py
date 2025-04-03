n = int(input())
nums = list(map(int, input().split()))

even = sum(1 for x in nums if x % 2 == 0)
odd = n - even

if even > odd:
    print("Happy")
else:
    print("Sad")
