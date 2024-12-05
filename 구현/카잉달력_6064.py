import sys
input = sys.stdin.readline

def cal_year(M, N, x, y):
    tmp = x
    while tmp <= M * N: # tmp의 범위는 M*N을 넘을 수 없다.
        if (tmp - x) % M == 0 and (tmp - y) % N == 0:
            return tmp
        tmp += M
    return -1

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().split())
        print(cal_year(M, N, x, y))