import sys
input = sys.stdin.readline

def permutation_input(vlist):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            permutation_input(vlist + [input_list[i]])
            visited[i] = 0
            
if __name__ == "__main__":
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    #오름차순 정렬
    input_list.sort()
    visited = [ 0 for _ in range(n) ]
    permutation_input(vlist)