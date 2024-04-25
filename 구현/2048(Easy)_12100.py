import sys 
input = sys.stdin.readline
import copy

def left(target_arr):
    for i in range(N):
        # 제일 왼쪽부터 채워져야 함, 현재 채워질 부분을 나타냄
        cursor = 0
        for j in range(N):
            if target_arr[i][j] != 0:
                tmp = target_arr[i][j]
                # 먼저 비우기
                target_arr[i][j] = 0
                
                # 비어있으면 옮김
                if target_arr[i][cursor] == 0:
                    target_arr[i][cursor] = tmp
                # 같은 값이면 합침
                elif target_arr[i][cursor] == tmp:
                    target_arr[i][cursor] *= 2
                    cursor += 1
                # 비어있지 않고 다른 값이면 pass후 원래 값으로 채워주기
                else:
                    cursor += 1
                    target_arr[i][cursor] = tmp
    return target_arr
    
def right(target_arr):
    for i in range(N):
        # 제일 오른쪽부터 채워져야 함
        cursor = N-1
        for j in range(N-1, -1, -1):
            if target_arr[i][j] != 0:
                tmp = target_arr[i][j]
                target_arr[i][j] = 0
                
                if target_arr[i][cursor] == 0:
                    target_arr[i][cursor] = tmp
                elif target_arr[i][cursor] == tmp:
                    target_arr[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    target_arr[i][cursor] = tmp            
    return target_arr

def up(target_arr):
    for i in range(N):
        # 제일 위쪽부터 채워져야 함
        cursor = 0
        for j in range(N):
            if target_arr[j][i] != 0:
                tmp = target_arr[j][i]
                target_arr[j][i] = 0
                
                if target_arr[cursor][i] == 0:
                    target_arr[cursor][i] = tmp
                elif target_arr[cursor][i] == tmp:
                    target_arr[cursor][i] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    target_arr[cursor][i] = tmp
    return target_arr

def down(target_arr):
    for i in range(N):
        # 제일 아래쪽부터 채워져야 함
        cursor = N-1
        for j in range(N-1, -1, -1):
            if target_arr[j][i] != 0:
                tmp = target_arr[j][i]
                target_arr[j][i] = 0
                
                if target_arr[cursor][i] == 0:
                    target_arr[cursor][i] = tmp
                elif target_arr[cursor][i] == tmp:
                    target_arr[cursor][i] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    target_arr[cursor][i] = tmp
    return target_arr
                    
def dfs(n, arr):
    global ans
    # 이동이 끝나면 arr에서 최댓값 찾기
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return
    
    # 상하좌우 탐색
    for i in range(4):
        # 상하좌우 케이스를 다 다르게 탐색해야 하므로 매번 deepcopy 해줘야 함
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(n+1, left(copy_arr))
        elif i == 1:
            dfs(n+1, right(copy_arr))
        elif i == 2:
            dfs(n+1, up(copy_arr))
        else:
            dfs(n+1, down(copy_arr))

if __name__ == "__main__" : 
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    
    dfs(0, board)
    print(ans)