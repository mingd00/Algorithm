import sys 
input = sys.stdin.readline

def main() :
    words = list(input().rstrip().split())
    print(len(words))

if __name__ == "__main__" :
    main()