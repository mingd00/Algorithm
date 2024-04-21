import sys 
input = sys.stdin.readline

def sugar(n):
    answer = 0
    while n >= 0:
        if n % 5 == 0:
            answer += (n // 5)
            print(answer)
            break
        # 5의 배수가 될 때까지 -3 해주면서 count 올리기
        n -= 3
        answer += 1
    else:
        print(-1)
        
if __name__ == "__main__" : 
    n = int(input())
    sugar(n)
    