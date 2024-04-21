import sys 
input = sys.stdin.readline

def atm(n, time):
    time.sort()
    answer = 0
    for i in range(n):
        answer += (n-i) * time[i]
    return answer

if __name__ == "__main__" : 
    n = int(input())
    time = list(map(int, input().split()))
    print(atm(n, time))
    