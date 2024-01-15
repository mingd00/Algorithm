import sys 
input = sys.stdin.readline
            
def combination(vlist, index) :
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(index, n):
        combination(vlist + [i+1], i+1)
            
if __name__ == "__main__" :
    index = 0
    vlist = []
    n, m = map(int, input().split())
    visited = [0 for _ in range(n)]
    combination(vlist, index)