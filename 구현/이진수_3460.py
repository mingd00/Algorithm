import sys
input = sys.stdin.readline

def cal(v):
    t = list(bin(v)[2:])[::-1]
    answer = [i for i in range(len(t)) if t[i] == '1']
    return answer

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        v = int(input())
        print(*cal(v))
