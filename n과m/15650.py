import sys 
input = sys.stdin.readline

def permutation_asc(vlist) :
    if len(vlist) == m:
        if vlist == sorted(vlist):
            print(*vlist)
            return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            permutation_asc(vlist + [i+1])
            visited[i] = 0
            
def combination(vlist, index) :
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(index, n):
        if visited[i] == 0:
            visited[i] = 1
            combination(vlist + [i+1], i+1)
            visited[i] = 0
            
if __name__ == "__main__" :
    index = 0
    vlist = []
    n, m = map(int, input().split())
    visited = [0 for i in range(n)]
    combination(vlist, index)