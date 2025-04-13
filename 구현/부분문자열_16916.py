import sys
input = sys.stdin.readline

def main():
    S = input().rstrip()
    P = input().rstrip()
    print(1) if P in S else print(0)

if __name__ == "__main__":
    main()
    
# 부분 문자열의 순서까지 고려해서 비교하려면 list로 감싸주면 됨