import sys 
import copy
from collections import deque
input = sys.stdin.readline

#바이러스 퍼뜨리기
def lab(copy_graph):
        #초기 바이러스 que에 append
        global virus    
        que = copy.deepcopy(virus)
        
        while que:
            x, y = que.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < row and 0 <= ny < col and copy_graph[ny][nx] == 0:
                    copy_graph[ny][nx] = 2
                    que.append((nx, ny)) 
        
        #각각의 경우의 수마다 바이러스가 퍼진 후의 0의 개수를 append        
        count_zeros.append(sum(row.count(0) for row in copy_graph)) 

#벽의 조합 찾기(3개)
def combination_zero(vlist, index, graph):
        if len(vlist) == 3:
            copy_graph = copy.deepcopy(graph)
            for vr, vc in vlist:
                copy_graph[vc][vr] = 1
            lab(copy_graph)
            return
                 
        for i in range(index, len(zeros)):
            if visited_zero[i] == 0:
                visited_zero[i] = 1
                combination_zero(vlist + [zeros[i]], index+1, graph)
                visited_zero[i] = 0
    
if __name__ == "__main__" : 
    col, row = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(col)]
    index = 0
    
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    #0, 2(virus)의 좌표 모음
    zeros = []
    virus = deque()
    for c in range(col):
        for r in range(row):
            if graph[c][r] == 0:
                zeros.append((r, c))
            elif graph[c][r] == 2:
                virus.append((r, c))
    
    #벽의 조합을 저장하기 위한 리스트      
    visited_zero = [0 for _ in range(len(zeros))]
    
    #바이러스 bfs
    count_zeros = []

    combination_zero([], index, graph)
                
    print(max(count_zeros))
                