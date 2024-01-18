import sys 
import heapq
input = sys.stdin.readline

def maximum_weight(jewelrys, bags):
    result = 0
    prices = []
    #bags안의 값들을 각각 보석의 무게와 비교
    for bag in bags:
        while jewelrys and bag >= jewelrys[0][0]:
            #최대힙으로 저장하기 위해 - 붙여서 삽입
            heapq.heappush(prices, -jewelrys[0][1])
            heapq.heappop(jewelrys) 
            
        if prices:
            result -= heapq.heappop(prices)          
            
    return result

def main() :
    #보석의 개수, 가방의 개수
    num_jewelry, num_bag = map(int, input().split())
    
    #보석의 무게, 가격 -> 보석의 개수만큼
    heapj = []
    for _ in range(num_jewelry):
        weight, price = map(int, input().split())
        heapq.heappush(heapj, (weight ,price))
        
    #가방에 담을 수 있는 최대 무게 -> 가방의 개수만큼
    bags = [int(input()) for _ in range(num_bag)]
    bags.sort()
    
    print(maximum_weight(heapj, bags))

if __name__ == "__main__" : 
    main()