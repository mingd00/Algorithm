import sys
input = sys.stdin.readline

def remote_controller(N, M, buttons):
    min_cnt = abs(100 - N)
    
    if N == 100:
        return 0 
    for i in range(1000001):
        for t in str(i):
            if t in buttons:
                break
        else:
            min_cnt = min(len(str(i)) + abs(N - i), min_cnt)
    return min_cnt

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    if M > 0:
        buttons = input().split()  # 고장난 버튼 목록
    else:
        buttons = []
    
    print(remote_controller(N, M, buttons))