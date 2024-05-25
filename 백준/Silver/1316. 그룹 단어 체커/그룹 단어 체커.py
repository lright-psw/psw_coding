n=int(input())

words = []
already = []
cnt = 0

for i in range(n):
    words.append(input())

for i in range(n):
    flag = 0
    already.clear()
    for j in range(1,len(words[i])):
        already.append(words[i][j-1])
        if words[i][j-1] == words[i][j]:
            if words[i][j] not in already:
                already.append(words[i][j])
        elif words[i][j-1] != words[i][j]:
            if  words[i][j] in already:
                flag = 1
            elif words[i][j] not in already:
                already.append(words[i][j])
    if flag == 0:
        cnt += 1

print(cnt)