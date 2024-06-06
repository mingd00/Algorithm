import sys
input = sys.stdin.readline
from collections import Counter

def main():
    n = int(input())
    nlist = []
    for _ in range(n):
        a, b = input().split()
        nlist.append(a)
    
    nlist_counter = Counter(nlist)
    res = []
    for name, record in nlist_counter.items():
        if record % 2 != 0:
            res.append(name)
    
    for r in sorted(res, reverse=True):
        print(r)
        
def main2():
    n = int(input())
    company = {}
    for _ in range(n):
        a, b = input().split()
        if b == 'enter':
            company[a] = True
        else:
            del company[a]
    
    print("\n".join(sorted(company.keys(), reverse=True)))

if __name__ == "__main__":
    main2()