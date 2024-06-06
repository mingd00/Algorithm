import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    sset = set(input().rstrip() for _ in range(N))
    cnt = 0

    for _ in range(M):
        s = input().rstrip()
        if s in sset:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()