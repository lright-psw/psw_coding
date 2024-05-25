# 0은 빈 칸, 1은 집, 2는 치킨집
# 집 < 2n / m <= 치킨집 <= 13

n,m = map(int,input().split())

c_map = []
h_map=[]
rst = 99999

#맵 만들기
for i in range(n):
    city = list(map(int,input().split()))
    for j in range(n):
        if city[j] == 1:
            h_map.append((i,j))
        elif city[j] == 2:
            c_map.append((i,j))
            

#치킨집 m개에 맞춰서 고르기
def choice_chiken(start):
    global rst
    #억제기 
    if sum(visited) == m:
        cnt = 0
        for i in range(len(h_map)): #집 하나당
            h_cnt = 999999 #최소 집이랑 가게 거리
            for j in range(len(visited)): #가게 거리
                if visited[j] == 1:
                    tmp_cnt = abs(h_map[i][0]-c_map[j][0]) + abs(h_map[i][1]-c_map[j][1]) # 지금계산한거 거리
                    h_cnt = min(h_cnt,tmp_cnt)
            cnt += h_cnt
        rst = min(rst,cnt)
        return 
    for i in range(start,len(c_map)):
        if visited[i] == 0:
            visited[i] = 1
            choice_chiken(i+1)
            visited[i] = 0


visited = [0 for _ in range(len(c_map))]
choice_chiken(0)
print(rst)


#치킨집이랑 집이랑 거리 구해주는 함수
# def find_len(h,c):
#     chicken_length = abs(h[0]-c[0]) + abs(h[1]-c[1])
#     return chicken_length

# #시간초과# #
#
#치킨집 m개에 맞춰서 고르기
# def choice_chiken():
#     global rst
#     global cnt
#     #억제기 
#     if len(ans) == m:
#         cnt = 0
#         # print(" ".join(map(str,ans)))
#         for i in range(len(h_map)): #집 하나당
#             h_cnt = math.inf #최소 집이랑 가게 거리
#             tmp_cnt = 0 # 지금계산한거 거리
#             for j in ans: #가게 거리
#                 tmp_cnt = find_len(h_map[i],c_map[j])
#                 h_cnt = min(h_cnt,tmp_cnt)
#             cnt += h_cnt
#         rst = min(rst,cnt)
#         return 
#     for i in range(len(c_map)):
#         if i not in ans and visited[i] == 0:
#             visited[i] = 1
#             ans.append(i)
#             choice_chiken()
#             visited[i] = 0
#             ans.pop()
