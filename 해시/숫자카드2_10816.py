import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
nlist = list(map(int, input().split()))
target_n = int(input())
target_nlist = list(map(int, input().split()))

# Counter 객체 생성
nlist_cnt = Counter(nlist)

res = [nlist_cnt[t] for t in target_nlist]

print(*res)