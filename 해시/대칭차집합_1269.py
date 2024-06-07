import sys
input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    Alist = set(map(int, input().split()))
    Blist = set(map(int, input().split()))
    
    print(len(Alist-Blist)+len(Blist-Alist))

if __name__ == "__main__":
    main()