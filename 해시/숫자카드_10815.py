import sys
input = sys.stdin.readline

def main():
    input()
    nlist = set(input().split())
    input()
    tlist = input().split()

    print(" ".join("1" if t in nlist else "0" for t in tlist))
if __name__ == "__main__":
    main()