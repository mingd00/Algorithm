import sys
import heapq
input = sys.stdin.readline

def dijkstra(maze, col, row, dx, dy):
    que = []
    distance = [[float('inf')]*row for _ in range(col)]
    heapq.heappush(que, (0, 0, 0))
    distance[0][0] = 0
    
    while que:
        count, x, y = heapq.heappop(que)
        
        if count > distance[y][x]:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 안에 있고 현재 경로에서의 count보다 이전 경로에서의 count가 더 짧을 경우
            if 0 <= nx < row and 0 <= ny < col and distance[ny][nx] > count + maze[y][x]:
                distance[ny][nx] = count + maze[y][x]
                heapq.heappush(que, (distance[ny][nx], nx, ny))

    return distance

def main():
    row, col = map(int, input().split())
    maze = [list(map(int, input().rstrip())) for _ in range(col)]
    
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    distance = dijkstra(maze, col, row, dx, dy)
    print(distance[col-1][row-1])
    
if __name__ == "__main__":
    main()
    

# BFS
# import sys 
# from collections import deque
# input = sys.stdin.readline

# def bfs(maze, row, col, dx, dy):
#     que = deque()
#     que.append((0, 0))
#     distance = [[-1]*row for _ in range(col)]
#     distance[0][0] = 0
    
#     while que:
#         x, y = que.popleft()      
            
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if 0 <= nx < row and 0 <= ny < col and distance[ny][nx] == -1:
#                 if maze[ny][nx] == 0:
#                     #벽이 없는 곳을 먼저 탐색
#                     que.appendleft((nx, ny))
#                     distance[ny][nx] = distance[y][x]
#                 else:
#                     que.append((nx, ny))
#                     distance[ny][nx] = distance[y][x] + 1
#     return distance 

# def main():
#     row, col = map(int, input().split())
#     maze = [list(map(int, input().rstrip())) for _ in range(col)]
    
#     #상하좌우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
    
#     distance = bfs(maze, row, col, dx, dy)
#     print(distance[col-1][row-1])
    
# if __name__ == "__main__" : 
#     main()
    
