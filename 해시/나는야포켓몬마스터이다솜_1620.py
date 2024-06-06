import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    pdic, rpdic = {}, {}
    for i in range(N):
        p = input().rstrip()
        pdic[i+1] = p
        rpdic[p] = i+1
    
    for _ in range(M):
        q = input().rstrip()
        if q.isdigit():
            print(pdic[int(q)])
        else:
            print(rpdic[q])
    
if __name__ == "__main__":
    main()