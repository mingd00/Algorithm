import sys 
input = sys.stdin.readline

def car():
    # 들어간 차량의 idx가 나간 차량 보다 큰게 하나라도 있으면 추월
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if car_in[car_out[i]] > car_in[car_out[j]]:
                cnt += 1
                break
            
    print(cnt)

if __name__ == "__main__" : 
    n = int(input())
    car_in, car_out = {}, []
    for i in range(n):
        num = input().rstrip()
        car_in[num] = i
    car_out = [input().rstrip() for _ in range(n)]

    car()
    
    