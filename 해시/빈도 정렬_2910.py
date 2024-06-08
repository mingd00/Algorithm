import sys 
input = sys.stdin.readline
from collections import Counter

# Counter를 쓰지 않는다면 dict으로 방문체크 해서 빈도 수 계산
# lambda함수로 value를 key로 해서 정렬한 후 작업 진행하면 될 듯 
def main():
    N, C = map(int, input().split())
    nlist = list(map(int, input().split()))
    
    f_nlist = Counter(nlist).most_common()
    
    for f in f_nlist:
        for _ in range(f[1]):
            print(f[0], end=' ')

if __name__ == "__main__" : 
    main()