import sys 
import heapq
input = sys.stdin.readline

def dijktra(start, input_distance) :
    #최단 거리는 무한대로 초기화
    distance = [float('inf') for _ in range(V+1)]
    #매개변수로 들어온 시작 정점까지의 최단 거리만 업데이트
    distance[start] = input_distance[start]
    
    que = []
    heapq.heappush(que, (input_distance[start], start))
    
    while que:
        dist, node = heapq.heappop(que)
        if dist > distance[node]:
            continue
        
        for next in graph[node]:
                n_node = next[0]
                n_dist = next[1] + distance[node]
                if distance[n_node] > n_dist:
                    distance[n_node] = n_dist
                    heapq.heappush(que, (n_dist, n_node))  
                
    return distance  

if __name__ == "__main__" : 
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        #양방향 입력
        graph[s].append((e, w))
        graph[e].append((s, w))
    #꼭 지나야 하는 정점
    v1, v2 = map(int, input().split())
    
    #최단 거리를 업데이트해 줄 리스트
    distance = [float('inf') for _ in range(V+1)]
    distance[1] = 0
     
    #V1 먼저 방문  
    v1_distance = dijktra(1, distance)
    v1_distance = dijktra(v1, v1_distance)
    v1_distance = dijktra(v2, v1_distance)
    
    #V2 먼저 방문  
    v2_distance = dijktra(1, distance)
    v2_distance = dijktra(v2, v2_distance)
    v2_distance = dijktra(v1, v2_distance)
    
    #최단 경로의 길이 출력
    if min(v1_distance[V], v2_distance[V]) == float('inf'):
        print(-1)
    else:
        print(min(v1_distance[V], v2_distance[V]))
    
