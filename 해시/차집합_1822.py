import sys
input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    aset = set(map(int, input().split()))
    bset = set(map(int, input().split()))
    ans = aset - bset
    print(len(ans))
    if len(ans) != 0:
        print(*sorted(ans))

if __name__ =="__main__":
    main()