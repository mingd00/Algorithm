import sys 
input = sys.stdin.readline

def main():
    n = int(input())
    cow = {}
    cnt = 0
    for _ in range(n):
        c, l = map(int, input().split())
        if c not in cow:
            cow[c] = l
        else:
            if cow[c] != l:
                cnt += 1
                cow[c] = l 
    
    print(cnt)

if __name__ == "__main__" : 
    main()