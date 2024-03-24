import sys 
input = sys.stdin.readline
from collections import deque

def main() :
    T = int(input())
    for _ in range(T):
        arr = deque()
        orders = input()
        n = int(input())
        arr = deque(input().rstrip()[1:-1].split(","))
        
        rev, flag = 0, 0
        # 공백 예외 처리
        if arr == deque(['']):
            arr = []
            
        for order in orders:
            if order == 'R':
                rev += 1
            elif order == 'D':
                if len(arr) == 0:
                    flag = 1
                    print('error')
                    break
                else:
                    if rev % 2 == 0:
                        arr.popleft()
                    else:
                        arr.pop()
                        
        # 에러를 출력하지 않았다면
        if flag == 0:
            # R이 짝수 개이면 그대로 출력
            if rev % 2 == 0:
                print("[" + ",".join(arr) + "]")
            # R이 홀수 개이면 역순으로 출력
            else:
                arr.reverse()
                print("[" + ",".join(arr) + "]")
        
if __name__ == "__main__" : 
    main()