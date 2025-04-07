import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        lst = list(map(int, input().split()))
        print(sorted(lst, reverse=True)[2])

if __name__ == "__main__":
   main()