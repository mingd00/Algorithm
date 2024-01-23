import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, graph, result):
    for i in graph[start]:
        if result[i] == 0:
            result[i] = start
            dfs(i, graph, result)
        
if __name__ == "__main__":
    n = int(input())
    #인접 리스트로 입력 받기
    graph = [[] for _ in range(n+1)]
    result = [0 for _ in range(n+1)]
    for _ in range(n-1):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    dfs(1, graph, result)

    for i in range(2, n+1):
        print(result[i])