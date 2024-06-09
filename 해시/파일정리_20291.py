import sys 
input = sys.stdin.readline
from collections import Counter

# Counter 클래스로 풀기 -> 220ms
def main():
    n = int(input())
    wlist = [list(input().rstrip().split('.'))[1] for _ in range(n)]
    wlist_counter = Counter(wlist).items()
    
    sorted_wlist_counter = sorted(wlist_counter, key=lambda x: x[0])
    for s in sorted_wlist_counter:
        print(s[0], s[1])
    
# 딕셔너리로 풀기 -> 172ms   
def main2():
    n = int(input())
    # 확장자 빈도 저장
    tdic = dict()
    for _ in range(n):
        _, extend = input().rstrip().split('.')
        if extend not in tdic:
            tdic[extend] = 0
        tdic[extend] += 1
    
    s_tdic = sorted(tdic.items(), key=lambda x: x[0])
    for st in s_tdic:
        print(st[0], st[1])
    
if __name__ == "__main__" : 
    main2()