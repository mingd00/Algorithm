import sys 
input = sys.stdin.readline

if __name__ == "__main__" : 
    n = int(input())
    vlist = []
    count = [1 for _ in range(n)]
    for _ in range(n):
        vlist.append(list(map(int, input().split())))
        
    for i in range(n):
        for j in range(n):
            if vlist[i][0] < vlist[j][0] and vlist[i][1] < vlist[j][1]:
                count[i] += 1
    print(*count)