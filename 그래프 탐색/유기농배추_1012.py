import sys 
from collections import deque
input = sys.stdin.readline

def check_bfs(graph, n, m, x, y):  
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    #시작 정점은 방문 했다고 가정
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
            
        

def main():
    global graph
    
    case = int(input())
    for _ in range(case):
        count = 0
        n, m, k = map(int, input().split())
        graph = [[0] * (n) for _ in range(m)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
            
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    check_bfs(graph, n, m, i, j)
                    count += 1
                    
        print(count)


if __name__ == "__main__" :
    main()



'''
문제: 유기농 배추 -> 연결된 리스트의 개수 찾기
알고리즘: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
느낀점: - 특정 인덱스에 값 추가 하기 insert(위치, 값)
       - graph에서(이중리스트) x, y의 범위와 위치 잘 확인하기, 처음에 모두 0으로 초기화 해줘야 함
       - bf + bfs방식 : 완전 탐색으로 1을 먼저 찾고 1을 찾으면 bfs로 들어가서 탐색, 탐색한 부분은 0으로 바꿔주고 다시 완전탐색으로 돌아와서 1을 찾고 bfs 반복
       - 시작 정점 잘 체크하기 이 문제같은 경우에는 완전탐색에서 1을 찾은 시점부터 bfs탐색이 들어가야 함
       - 그래프의 범위 잘 확인하기 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1) -> M*N, X(0 ≤ X ≤ M), Y(0 ≤ Y ≤ N) -> (M+1)*(N+1)
'''