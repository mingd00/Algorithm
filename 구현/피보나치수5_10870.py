import sys
input = sys.stdin.readline

def cal(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    sum = cal(n-1) + cal(n-2)
    
    return sum
        
if __name__ == "__main__":
    n = int(input())
    print(cal(n))