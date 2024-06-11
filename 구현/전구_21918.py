import sys 
input = sys.stdin.readline

def light():
    for o in orders:
        if o[0] == 1:
            nlist[o[1]-1] = o[2]
        elif o[0] == 2:
            for i in range(o[1]-1, o[2]):
                if nlist[i] == 1:
                    nlist[i] = 0
                else:
                    nlist[i] = 1
        elif o[0] == 3:
            for i in range(o[1]-1, o[2]):
                nlist[i] = 0
        else:
            for i in range(o[1]-1, o[2]):
                nlist[i] = 1
                
    print(*nlist)

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    orders = [list(map(int, input().split())) for _ in range(M)]
    light()