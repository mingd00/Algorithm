import sys
input = sys.stdin.readline

def floyd(city, graph):
  for k in range(1, city+1):
    for i in range(1, city+1):
      for j in range(1, city+1):
        graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
        
  return graph 

def main():
  city = int(input())
  bus = int(input())
  #최단 거리 리스트 무한대로 초기화
  graph = [[float('inf')]*(city+1) for _ in range(city+1)]
  
  #자기 자신으로 가는 거리는 0
  for i in range(1, city+1):
    graph[i][i] = 0
  
  for _ in range(bus):
    s, e, w = map(int, input().split())
    #같은 시작 정점 -> 끝 정점이 들어올 경우 더 작은 값으로 넣기
    graph[s][e] = min(graph[s][e], w)
    
  distance = floyd(city, graph)
  
  for i in range(1, city+1):
    for j in range(1, city+1):
      #i->j로 갈 수 없는 경우 0출력
      if distance[i][j] == float('inf'):
        distance[i][j] = 0
    print(*distance[i][1:])
         
if __name__ == "__main__":
  main()