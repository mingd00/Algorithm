import sys
input = sys.stdin.readline
from collections import Counter

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        vlist = []
        cnt = 1
        for _ in range(n):
            a, b = input().rstrip().split()
            vlist.append(b)
        
        vlist_counter = Counter(vlist)
        for key in vlist_counter:
            cnt *= vlist_counter[key] + 1
        
        print(cnt-1)
        
if __name__ == "__main__":
    main()