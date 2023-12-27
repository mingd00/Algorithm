import sys 
from collections import deque
input = sys.stdin.readline

def dfs(start) :
    visited_dfs[start] = True
    print(start, end=" ")
    
    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited_bfs[start] = True
    
    while q:
        v = q.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                q.append(i)
                          

if __name__ == "__main__" :
    #정점, 간선, 시작점
    n, e, start = map(int, input().split())
    
    #인접 리스트 초기화
    graph = [[] for _ in range(n+1)]
    
    #방문 체크
    visited_dfs = [False] * (n+1)
    visited_bfs = [False] * (n+1)
    
    #인접 리스트 input
    for i in range(e):
        n1, n2 = list(map(int, input().split()))
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    #인접 리스트 정렬
    for i in graph:
        i.sort()
    
    dfs(start)
    print()
    bfs(start)
    
'''
문제: DFS, BFS
알고리즘: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
느낀점: 인접 리스트 요소를 sort()해줘야 순서대로 탐색 가능
'''


