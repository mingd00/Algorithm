import sys 
input = sys.stdin.readline

def coin(N, K):
    count = 0
    while K > 0:
        for i in range(N):
            if K < coins[i]:
                continue
            else:
                count += K // coins[i]
                K %= coins[i]
    return count

if __name__ == "__main__" : 
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    coins.sort(reverse=True)
    
    print(coin(N, K))
    