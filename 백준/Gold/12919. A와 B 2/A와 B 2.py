from collections import deque

s = list(input())
t = list(input())
rst = 0
#test print
# print(len(s))
# print(len(t))

# logic funtion
def bfs(tmp):
    global rst
    # end point
    # print(tmp)
    # print(len(s), len(tmp))
    if len(s) == len(tmp):
        if tmp == s:
            rst = 1
            return
        return
    #logic
    if tmp[-1] == "A":
        tmp.pop()
        bfs(tmp)
        tmp.append("A")
    if tmp[0] == "B":
        tmp.reverse()
        tmp.pop()
        bfs(tmp)
        tmp.append("B")
        tmp.reverse()

bfs(t)
print(rst)