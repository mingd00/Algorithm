import sys 
input = sys.stdin.readline
from collections import defaultdict
import heapq

# target이 되는 값이 solved 명령에 해당하는 번호인지 체크
def solved_process(h):
    while solved[abs(h[0][1])] != 0:
        solved[abs(h[0][1])] -= 1
        heapq.heappop(h)

# 명령 처리 함수
def system(order):
    if order[0] == 'recommend':
        if order[1] == '1':
            # 레벨이 가장 높은 문제 출력
            solved_process(maxH)
            print(-maxH[0][1])
        else:
            # 레벨이 가장 낮은 문제 출력
            solved_process(minH)
            print(minH[0][1])
    elif order[0] == 'add':
        num, level = int(order[1]), int(order[2])
        heapq.heappush(minH, (level, num))
        heapq.heappush(maxH, (-level, -num))
    else:
        num = int(order[1])
        # 문제 번호가 key
        solved[num] += 1

if __name__ == "__main__" : 
    N = int(input())
    minH, maxH = [], []
    solved = defaultdict(int)
    
    for _ in range(N):
        num, level = map(int, input().split())
        heapq.heappush(minH, (level, num))
        heapq.heappush(maxH, (-level, -num))
        
    M = int(input())
    orders = [list(input().rstrip().split()) for _ in range(M)]
    
    for o in orders:
        system(o)
    