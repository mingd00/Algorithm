import sys
input = sys.stdin.readline

def main():
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))
    print(H, W, heights)

if __name__ == "__main__":
    main()