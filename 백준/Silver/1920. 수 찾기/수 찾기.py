import sys
import heapq

input = sys.stdin.readline

def binary_search(arr, target, st, end):
    if st>end:
        return 0
    mid = (st + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr,target,st,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)

def main():
    N = int(input().strip())
    A = list(map(int,input().strip().split()))
    M = int(input().strip())
    X = list(map(int,input().strip().split()))
    
    A.sort()
    
    for x in X:
        print(binary_search(A,x,0,N-1))
    

if __name__=="__main__":
    main()