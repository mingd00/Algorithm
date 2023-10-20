import sys 
input = sys.stdin.readline

def nm3(vlist) :
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        nm3(vlist + [i+1])

if __name__ == "__main__" :
    vlist = []
    n, m = map(int, input().split())
    nm3(vlist)