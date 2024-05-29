import sys
input = sys.stdin.readline
from collections import Counter

name = input().rstrip()
name_dict = Counter(name)
res = ''
ans = 0
mid = ''

# 홀수가 한 개면 중간값으로 설정, 2개 이상이면 
for k, v in list(name_dict.items()):
    if v % 2 == 1:
        mid = k
        ans += 1   
        if ans > 1:
            print("I'm Sorry Hansoo")
            exit()
            
for k, v in sorted(name_dict.items()):
    res += k * (v//2)

print(res + mid + res[::-1])