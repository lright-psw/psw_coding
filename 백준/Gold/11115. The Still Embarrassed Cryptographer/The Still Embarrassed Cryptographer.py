import sys
input = sys.stdin.readline

def find_cycle_length(c_map, s):
    seen = s
    for q in range(1, 10001):
        seen = ''.join(c_map.get(ch, '?') for ch in seen)
        if '?' in seen:
            return "mjau"
        if seen == s:
            return q
    return "mjau"

def process_case(S, T):
    if S == T:
        return 0  # crypt(S)==S → r = 1, 그러면 q = r-1 = 0

    c_map = {}
    for s_ch, t_ch in zip(S, T):
        if s_ch in c_map:
            if c_map[s_ch] != t_ch:
                return "mjau"  # 모순 발생
        c_map[s_ch] = t_ch

    # injective 함수인지 확인 (서로 다른 s는 서로 다른 t로 가야 함)
    if len(set(c_map.values())) != len(c_map):
        return "mjau"

    cycle = find_cycle_length(c_map, S)
    if cycle == "mjau":
        return "mjau"
    else:
        # crypt^(cycle)(S)=S 인데, 문제에서 원하는 q는 crypt^q(crypt(S))=S 즉, q = cycle - 1
        return cycle - 1

# 입력 처리
n = int(input())
for _ in range(n):
    S = input().strip()
    T = input().strip()
    print(process_case(S, T))
