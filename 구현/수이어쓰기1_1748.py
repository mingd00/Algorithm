import sys
input = sys.stdin.readline

N = int(input())

tmp = len(str(N)) 
cnt = (N - 10 ** (tmp - 1) + 1) * tmp

for i in range(1, tmp):
    cnt += 9 * 10 ** (i-1) * i
    
print(cnt)