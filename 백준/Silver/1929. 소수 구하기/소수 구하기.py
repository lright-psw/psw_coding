def eratosthenes(N,M):
    is_prime = [True] *(M+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(M*0.5) + 1):
        if is_prime[i]:
            for j in range(i*i,M+1,i):
                is_prime[j] = False
                
    for i in range(N,M+1):
        if is_prime[i]:
            print(i)

N, M = map(int, input().split())
eratosthenes(N, M)
