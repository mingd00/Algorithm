import sys 
input = sys.stdin.readline

def step():
    for i in range(1, n):
        for j in range(i):
            if slist[i] > slist[j]:
                dp_list[i] = max(dp_list[i], dp_list[j]+1)
                
    return dp_list

if __name__ == "__main__" : 
    n = int(input())
    slist = list(map(int, input().split()))
    dp_list = [1 for _ in range(n)]
    dp = step()
    print(max(dp))