import sys 
input = sys.stdin.readline
from collections import deque

def knight_move(n, graph, x, y, ex, ey):
    #나이트가 이동할 수 있는 방향
    dx = [-1,-1,-2,-2,1,1,2,2]
    dy = [-2,2,1,-1,-2,2,1,-1]
    
    que = deque()
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
        
        if x == ex and y == ey:
            return graph[x][y] 
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 체크, 방문 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] != 0:
                continue
            
            graph[nx][ny] = graph[x][y] + 1
            que.append((nx, ny))

def main():
    result = []
    case = int(input())
    for _ in range(case):
        n = int(input())
        graph = [[0]*n for _ in range(n)]
        s1, s2 = map(int, input().split())
        e1, e2 = map(int, input().split())
        c = knight_move(n, graph, s1, s2, e1, e2)
        result.append(c)
        
    for i in result:
        print(i)

if __name__ == "__main__" :
    main()