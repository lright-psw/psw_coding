arival = []
term = []

def main():
    rst = 0
    N, K = map(int, input().split())

    for _ in range(N):
        arival.append(int(input()))

    for i in range(1,N):
        term.append(arival[i] - arival[i-1] - 1)
    
    term.sort()

    for i in range(N-K):
        rst += int(term[i])
    
    rst += N

    if K >= N:
        print(N)
        return
    
    print(rst)


if __name__ == "__main__":
    main()