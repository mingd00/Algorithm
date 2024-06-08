import sys 
input = sys.stdin.readline
from collections import Counter

def main():
    n = int(input())
    nlist = [int(input()) for _ in range(n)]
    
    nlist_counter = list(Counter(nlist).items())
    ans = sorted(nlist_counter, key=lambda x: [-x[1], x[0]])
    print(ans[0][0])

if __name__ == "__main__" : 
    main()