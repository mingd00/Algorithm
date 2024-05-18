import sys 
input = sys.stdin.readline

if __name__ == "__main__" : 
    n = int(input())
    line = 1
    # 대각선 기준 몇 번째줄(line) 몇 번째(n) 요소인지
    while n > line:
        n -= line
        line += 1
        
    # 짝수줄 -> 분자는 1부터 증가, 분모는 line부터 감소
    # 홀수줄 -> 분자는 line부터 감소, 분모는 1부터 증가
    if line % 2 == 0:
        a = n
        b = line-n+1
    else:
        a = line-n+1
        b = n

    print(a, '/', b, sep='')