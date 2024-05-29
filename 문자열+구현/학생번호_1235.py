import sys
input = sys.stdin.readline

n = int(input())
vlist = [list(input().split()) for _ in range(n)]
target = len(vlist[0][0])

for i in range(1, target+1):
    n_vlist = list(map(lambda x: x[0][target-i:target], vlist))
    if len(set(n_vlist)) == len(vlist):
        print(i)
        exit()
    else:
        continue