import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, v, graph):
  distance = [float('inf') for _ in range(v+1)]
  distance[start] = 0
  que = []
  heapq.heappush(que, (0, start))
  
  while que:
    dist, node = heapq.heappop(que)
    #(?~현재)까지의 거리 > (처음~현재)까지의 거리
    if dist > distance[node]:
      continue
      
    for next in graph[node]:
      n_node = next[0]
      #(현재~다음)까지의 최단 거리 + (시작~현재)까지의 최단 거리
      n_dist = next[1] + distance[node]
      if distance[n_node] > n_dist:
        distance[n_node] = n_dist
        heapq.heappush(que, (n_dist, n_node))
         
  return distance
  
def main():
  v, e, target = map(int, input().split())
  graph = [[] for _ in range(v+1)]
  for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))    
  
  #오고 가는 시간의 최댓값을 출력
  result = 0
  for i in range(1, v+1):
    go = dijkstra(i, v, graph)
    back = dijkstra(target, v, graph)
    result = max(result, go[target] + back[i])
    
  print(result)
  
if __name__ == "__main__":
  main()

  
  