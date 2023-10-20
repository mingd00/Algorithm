import sys 
input = sys.stdin.readline

def nm2(vlist) :
    if len(vlist) == m:
        if vlist == sorted(vlist):
            print(*vlist)
            return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            nm2(vlist + [i+1])
            visited[i] = 0
            
if __name__ == "__main__" :
    vlist = []
    n, m = map(int, input().split())
    visited = [0 for i in range(n)]
    nm2(vlist)