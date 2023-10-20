import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def nm3(vlist, index) :
    if len(vlist) == m: 
        print(*vlist)
        return
    
    for i in range(index, n):
        nm3(vlist + [i+1], i)

if __name__ == "__main__" :
    vlist = []
    index = 0
    n, m = map(int, input().split())
    nm3(vlist, index)