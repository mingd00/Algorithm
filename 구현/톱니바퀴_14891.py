import sys 
input = sys.stdin.readline
from collections import deque
import copy

def cogwheel(wheels):
    target_w = copy.deepcopy(wheels)
    for i in range(K):
        wheels = copy.deepcopy(target_w)
        w = orders[i][0] - 1
        order = orders[i][1]
        if order == 1:
            target_w[w].appendleft(target_w[w].pop())
        else:
            target_w[w].append(target_w[w].popleft())
            
        # 오른쪽 톱니바퀴 검사
        rw = w
        copy_o = order
        while True:
            if 0 <= rw+1 < 4:
                rw += 1
                if wheels[rw-1][2] != wheels[rw][6]:
                    # 반대 방향으로 회전
                    copy_o *= -1
                    if copy_o == 1:
                        target_w[rw].appendleft(target_w[rw].pop())
                    else:
                        target_w[rw].append(target_w[rw].popleft())
                else:
                    break
            else:
                break
            
        # 왼쪽 톱니바퀴 검사
        lw = w
        while True:
            if 0 <= lw-1 < 4:
                lw -= 1
                if wheels[lw][2] != wheels[lw+1][6]:
                    # 반대 방향으로 회전
                    order *= -1
                    if order == 1:
                        target_w[lw].appendleft(target_w[lw].pop())
                    else:
                        target_w[lw].append(target_w[lw].popleft())
                else:
                    break
            else:
                break 
            
    return target_w

if __name__ == "__main__" : 
    answer = 0
    wheels = []
    orders = []
    for _ in range(4):
        wheels.append(deque(map(int, list(input().rstrip()))))

    K = int(input())
    for _ in range(K):
        orders.append(list(map(int, input().split())))
        
    nw = cogwheel(wheels)
    
    # 점수 계산
    for i in range(4):
        if i == 0 and nw[i][0] == 1:
            answer += 1
        elif i == 1 and nw[i][0] == 1:
            answer += 2 
        elif i == 2 and nw[i][0] == 1:
            answer += 4
        elif i == 3 and nw[i][0] == 1:
            answer += 8
            
    print(answer)