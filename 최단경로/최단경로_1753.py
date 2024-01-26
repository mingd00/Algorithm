import sys 
import heapq
input = sys.stdin.readline

def dijkstra():
    #최소 거리로 계속 업데이트 해주기 위해 무한대로 설정
    distance = [float('inf') for _ in range(V+1)]
    distance[start] = 0
    
    que = []
    #시작 정점~현재 정점 거리, 현재 정점
    heapq.heappush(que, (0, start))
    
    while que:
        dist, node = heapq.heappop(que)
        #(처음 ~ 현재 노드)보다 (? ~ 현재 노드)의 거리가 더 크다면 업데이트 할 필요X
        if dist > distance[node]:
            continue
        
        #현재 노드와 연결된 값을 탐색하며 최소 거리로 업데이트
        for next in graph[node]:
            n_node = next[0]
            #(처음 ~ 현재 노드) + (현재 노드 ~ 다음 노드) 
            n_dist = next[1] + distance[node]
            if distance[n_node] > n_dist:
                distance[n_node] = n_dist
                #(처음 ~ 다음 노드)의 최솟값, 다음 노드를 push
                heapq.heappush(que, (n_dist, n_node))
    
    return distance

if __name__ == "__main__" : 
    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V+1)]   
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        
    total_distance = dijkstra()
    for i in range(1, len(total_distance)):
        if total_distance[i] == float('inf'):
            print('INF')
        else:
            print(total_distance[i])