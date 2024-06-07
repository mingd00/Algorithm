import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    info = {}
    for _ in range(N):
        link, pwd = input().rstrip().split()
        info[link] = pwd
    for _ in range(M):
        target = input().rstrip()
        print(info[target])

if __name__ == "__main__":
    main()