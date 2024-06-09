import sys 
input = sys.stdin.readline

# Dictionary 사용 -> 1108ms
def main():
    N, M = map(int, input().split())
    memo = dict()
    
    for _ in range(N):
        m = input().rstrip()
        memo[m] = True
       
    for _ in range(M):
        cnt = 0
        blog = list(input().rstrip().split(','))
        for b in blog:
            if b in memo:
                if memo[b] == True:
                    cnt += 1
                    memo[b] = False
        print(N - cnt)
        N -= cnt

# Set 사용 -> 764ms    
def main2():
    N, M = map(int, input().split())
    memo = set(input().rstrip() for _ in range(N))
    
    for _ in range(M):
        blog = list(input().rstrip().split(','))
        for b in blog:
            memo.discard(b)
        print(len(memo))

if __name__ == "__main__" : 
    main2()
