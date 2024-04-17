# 고려해야 할점
# 폰켓몬은 N마리 중 절반만 가져갈 수 있다.
# 다른 종류의 폰켓몬을 가져갈 수 있는 최대치를 구하는 문제
# 이건 입출력을 내가 안하는듯?
def solution(nums):
    p_type = len(set(nums))
    take = len(nums)//2
    answer = min(take,p_type)
    return answer