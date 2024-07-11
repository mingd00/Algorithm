import sys
input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    S = list(map(int, input().split()))
    status = list(range(N))
    
    for cnt in range(150000):
        # 순서가 맞는지 체크
        for i in range(N):
            if P[status[i]] != i % 3:
                break
        # 순서가 다 맞다면
        else:
            print(cnt)
            break
        
        # 순서가 맞지 않다면 -> 섞어주기
        new_status = [None] * N
        for i in range(N):
            new_status[S[i]] = status[i]
        status = new_status
            
    # 아무리 섞어도 순서가 맞지 않다면
    else:
        print(-1)
    
if __name__ == "__main__":
    main()
    
    
    
    