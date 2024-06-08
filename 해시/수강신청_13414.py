import sys 
input = sys.stdin.readline

def main():
    K, L = map(int, input().split())
    ndic = dict()
    for _ in range(L):
        num = input().rstrip()
        if num not in ndic:
            ndic[num] = True
        else:
            del ndic[num]
            ndic[num] = True
    
    print("\n".join(list(ndic.keys())[:K]))

if __name__ == "__main__" : 
    main()
    