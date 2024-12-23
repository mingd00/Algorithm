import sys
input = sys.stdin.readline

def cal(n):
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n] 

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(cal(n))
    
    
'''
패턴 찾기
dp[1] = 1: 1
dp[2] = 2: 1+1, 2
dp[3] = 4: 1+1+1, 1+2, 2+1, 3
dp[4] = 7: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
dp[5] = 13: 1+1+1+1+1, 1+1+1+2->4개, 1+1+3->3개, 1+2+2->3개, 2+3->2개

i >= 4라면, dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
'''