a = int(input())
w, v = map(int, input().split())

adapter_amp = w // v  # 정수 나눗셈: 문제에서 분수 안 나옴 보장

if adapter_amp >= a:
    print(1)
else:
    print(0)
