import sys
input = sys.stdin.readline
from collections import Counter

def main():
    n = int(input())
    blist = [input().rstrip() for _ in range(n)]
    bestseller = Counter(blist).most_common()
    
    res = []
    for b in bestseller:
        if b[1] == bestseller[0][1]:
            res.append(b[0])
    
    print(sorted(res)[0])
    
def main2():
    n = int(input())
    bdic = {}
    for _ in range(n):
        book = input().rstrip()
        if book not in bdic:
            bdic[book] = 0
        bdic[book] += 1
    
    res = []    
    for b in bdic.keys():
        if bdic[b] == max(bdic.values()):
            res.append(b)
    
    print(sorted(res)[0])
        
if __name__ == "__main__":
    main()