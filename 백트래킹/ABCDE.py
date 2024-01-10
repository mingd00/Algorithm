import sys 
input = sys.stdin.readline


def dfs(start, visited_list, adj, count):
    visited_list[start] = True
    
    # 5개가 인접해 있는 것이 확인되면 1을 출력하고 프로그램 종료
    if count == 5:
        print(1)
        exit()
    
    for v in adj[start]:
        if not visited_list[v]:
            visited_list[v] = True
            dfs(v, visited_list, adj, count+1)
            # 백트래킹(-> 이 부분 때문에 백트래킹이 되는 것. 없으면 재귀)
            visited_list[v] = False
            
 
def main() :
    n, m = map(int, input().split())
    visited_list = [False] * n
    
    # 인접 리스트 생성
    adj = [[] for _ in range(n)]
    for _ in range(m):
        f1, f2 = map(int, input().split())
        adj[f1].append(f2)
        adj[f2].append(f1)
    
    # 모든 인접 경우의 수를 봐주기    
    for i in range(n):
        dfs(i, visited_list, adj, 1)
        visited_list[i] = False
        
    print(0)
    

if __name__ == "__main__" : 
    main()