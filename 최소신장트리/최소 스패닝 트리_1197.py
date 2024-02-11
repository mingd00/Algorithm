import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def prim(start):
    # 최소 신장 트리 리스트
    mst = []
    
    # 전체 가중치
    total_weight = 0
    
    # 시작 정점 가중치는 0
    heapq.heappush(mst, (0, start))
    
    while mst:
        w, v = heapq.heappop(mst)
        # 뺀 노드를 방문하지 않은 경우
        if visited[v] == 0:
            visited[v] = 1
            total_weight += w
            
            # 인접 간선 탐색
            for edge in graph[v]:
                heapq.heappush(mst, edge)
                    
    return total_weight

if __name__ == "__main__":
    # 정점, 간선
    n, m = map(int, input().split())
    # 빈 그래프 생성
    graph = defaultdict(list)
    visited = [0] * (n+1)
    
    # 무방향 그래프
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
        graph[e].append((w, s))
        
    print(prim(1))
    