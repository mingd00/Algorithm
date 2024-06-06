import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
vlist = [input().rstrip() for _ in range(N+M)]
res = []

vlist_counter = Counter(vlist)
for char, cnt in vlist_counter.items():
    if cnt > 1:
        res.append(char)
        
print(len(res))
for r in sorted(res):
    print(r)
        