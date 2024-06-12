import sys 
input = sys.stdin.readline
from itertools import combinations

def main():
    n = int(input())
    nlist = list(map(int, input().split()))
    nset = set()
    for i in range(1, len(nlist)+1):
        for combo in combinations(nlist, i):
            nset.add(sum(combo))
    
    print(sum(nlist)-len(nset))

if __name__ == "__main__" : 
    main()