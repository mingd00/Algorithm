import sys 
import heapq
input = sys.stdin.readline

def dijkstra():
    distance = [float('inf') for _ in range(city+1)]
    distance[start] = 0
    que = []   
    heapq.heappush(que, (0, start))
    
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
    city = int(input())
    bus = int(input())
    graph = [[] for _ in range(city+1)]
    for _ in range(bus):
        #출발, 도착, 버스 비용
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    start, end = map(int, input().split())   
    
    total_distance = dijkstra()
    print(total_distance[end]) 
    
    