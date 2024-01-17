import sys
import heapq
input = sys.stdin.readline

def greedy(heap_list):
    count = 0
    
    while heap_list:
        v1 = heapq.heappop(heap_list)
        v2 = heapq.heappop(heap_list)
        add = v1 + v2
        count += add
        
        heapq.heappush(heap_list, add)
        
        #남은 값이 하나 뿐이라면 더 이상 비교할 대상이 없으니 count return
        if len(heap_list) == 1:
            return count
    
def main():
    heap_list = []
    n = int(input())
    for _ in range(n):
        value = int(input())
        heapq.heappush(heap_list, value)
    
    #입력 요소가 하나라면 비교할 필요가 없으니 0 출력    
    if len(heap_list) == 1:
        print(0)
    else:
        print(greedy(heap_list))
 
if __name__ == "__main__":
    main()