import sys
input = sys.stdin.readline

def cal(N, K):
    target = []
    answer = 0
    for i in range(1, N+1):
        if N % i == 0:
            target.append(i)
    
    if len(target) >= K:
        answer = target[K-1]
    
    return answer

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    print(cal(N, K))