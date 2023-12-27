import sys
input = sys.stdin.readline

def virus(start):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            count[0] += 1
            virus(i)
            

if __name__ == "__main__":
    #시작 정점
    start = 1
    
    #연결된 리스트마다 count
    count = [0]
    
    #정점, 간선
    n = int(input())
    e = int(input())
    
    #방문 체크
    visited = [False] * (n+1)
    
    #인접 리스트
    graph = [[] for _ in range(n+1)]
    
    for i in range(e):
        n1, n2 = list(map(int, input().split()))
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    for i in graph:
        i.sort()
        
    virus(start)
    print(count[0])
        
    

'''
문제: 바이러스 -> 연결되어 있으면 감염
알고리즘: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
느낀점: dfs로 탐색하는 과정에서 하나를 탐색할 때마다 count+=1, 
        main에 있는 변수를 함수 안에서 쓰기만 한다면 global 선언을 하지 않아도 되지만 수정하려면 함수 안에서 global 선언이 필요하다.
        단, 리스트나 튜플은 내부의 원소 값을 바꾸는 것이기 때문에 가능하다.(리스트나 튜플 자체를 바꾸는 것은 불가능)
        -> 참조(O), 재정의(x)
'''