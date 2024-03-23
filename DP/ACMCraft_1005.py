import sys 
input = sys.stdin.readline
from collections import deque

def main() :
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        time = [0] + list(map(int, input().split())) # 건설 시간
        graph = [[] for _ in range(N+1)] # 건설 순서 규칙
        inDegree = [0 for _ in range(N+1)] # 진입 차수
        DP = [0 for _ in range(N+1)] # 해당 건물까지 걸리는 시간
        
        # 건설 규칙 저장
        for _ in range(K):
            a, b = map(int, input().split())
            graph[a].append(b)
            inDegree[b] += 1
            
        que = deque()
        # 진입차수 0인 거 큐에 넣기
        for i in range(1, N+1):
            if inDegree[i] == 0:
                que.append(i)
                DP[i] = time[i]
                
        while que:
            a = que.popleft()
            for i in graph[a]:
                inDegree[i] -= 1
                # DP를 이용해 건설 비용 갱신
                DP[i] = max(DP[a] + time[i], DP[i])
                if inDegree[i] == 0:
                    que.append(i)
            
        target = int(input())
        print(DP[target])
        
if __name__ == "__main__" : 
    main()