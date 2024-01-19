import sys 
import heapq
input = sys.stdin.readline

def cal(zero, one, minus, plus):
    result = 0
    for _ in range(one):
        result += 1
        
    while plus:
        if len(plus) == 1:
            #-를 붙여서 넣어줬으므로 빼줘야 함
            result -= heapq.heappop(plus)
            break
        
        result += heapq.heappop(plus)*heapq.heappop(plus)
    
    while minus:
        if len(minus) == 1:
            if zero:
                heapq.heappop(minus)
            else:
                result += heapq.heappop(minus)
            break
        
        result += heapq.heappop(minus)*heapq.heappop(minus)
        
    print(result)             

def seperate(vlist):
    zero = False
    one = 0
    minus = []
    plus = []
    for v in vlist:
        if v == 0:
            zero = True
        elif v == 1:
            one += 1
        elif v > 0:
            #최대힙으로 저장하기 위해 -붙이기
            heapq.heappush(plus, -v)
        else:
            heapq.heappush(minus, v)
        
    cal(zero, one, minus, plus)
        
def main() :
    n= int(input())
    vlist = []
    for _ in range(n):
        vlist.append(int(input()))
    
    seperate(vlist)

if __name__ == "__main__" : 
    main()