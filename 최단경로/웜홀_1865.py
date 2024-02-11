import sys
input = sys.stdin.readline

def Bellman(V, graph, start):
    # 간선의 가중치 W의 최댓값은 10000이다
    distance = [10001 for _ in range(V+1)]
    distance[start] = 0
    
    for i in range(1, V+1):
        for cur in range(1, V+1):
            for next, cost in graph[cur]:
                if distance[next] > distance[cur] + cost:
                    distance[next] = distance[cur] + cost
                
                    # 사이클 발생(V번 반복했을 때 값이 변함)
                    if i == V-1:
                        return True
    return False

def main():
    TC = int(input())
    for _ in range(TC):
        V, L, W = map(int, input().split())
        graph = [[] for _ in range(V+1)]
        #도로
        for _ in range(L):
            s, e, w = map(int, input().split())
            graph[s].append((e, w))
            graph[e].append((s, w))
        #웜홀
        for _ in range(W):
            s, e, w = map(int, input().split())
            graph[s].append((e, -w))
            
        if Bellman(V, graph, 1):
            print('YES')
        else:
            print('NO')
    
if __name__ == "__main__":
    main()