import sys 
input = sys.stdin.readline

def stock():
    j, s = n, n
    jcnt, scnt = 0, 0
    
    # 살 수 있을 때 전부 매수
    for i in range(len(stocks)):
        if stocks[i] <= j:
            jcnt += j // stocks[i]
            j %= stocks[i]
    
    # 3일 오르면 전액 매수, 3일 하락하면 전액 매도
    up, down, target, buy = 0, 0, 13, False
    for i in range(1, 14):
        # 전일 대비 하락 체크
        if stocks[i] < stocks[i-1]:
            down += 1
            up = 0
        elif stocks[i] > stocks[i-1]:
            up += 1
            down = 0
        else:
            up = 0
            down = 0
        
        if down >= 3 and stocks[i] <= s:
            scnt += s // stocks[i]
            s %= stocks[i]
            buy = True
            
        elif up >= 3 and buy == True:
            target = i
            up = 0
       
    jasset = jcnt * stocks[-1] + j
    sasset = scnt * stocks[target] + s
    
    if jasset > sasset:
        print("BNP")
    elif jasset < sasset:
        print("TIMING")
    else:
        print("SAMESAME")
        
if __name__ == "__main__" : 
    n = int(input())
    stocks = list(map(int, input().split()))
    stock()