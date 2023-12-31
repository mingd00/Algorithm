import sys 
input = sys.stdin.readline

def permutation(vlist) :
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            permutation(vlist+[i+1])
            visited[i] = 0   
            
if __name__ == "__main__" :
    vlist = []
    n, m = map(int, input().split())
    visited = [0 for _ in range(n)]
    permutation(vlist)
    
    
    