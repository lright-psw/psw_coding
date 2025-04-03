def convert_to_base(x, b):
    if x == 0:
        return "0"

    digits = []
    is_negative_base = b < 0
    abs_b = abs(b)

    while x != 0:
        r = x % abs_b
        x = (x - r) // b
        digits.append(str(r))

    return ''.join(reversed(digits))

x, b = map(int, input().split())

# 양의 진법이고 x < 0일 때만 '-' 붙여 출력
if b > 0 and x < 0:
    print('-' + convert_to_base(-x, b))
else:
    print(convert_to_base(x, b))
