N = int(input().strip())

q = []

for _ in range(N):
    line = input().strip().split()

    if line[0] == "push":
        q.append(int(line[1]))

    elif line[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            del q[0]

    elif line[0] == "size":
        print(len(q))

    elif line[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif line[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif line[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
