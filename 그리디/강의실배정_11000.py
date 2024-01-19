import sys 
import heapq
input = sys.stdin.readline

def classroom(times):  
    room = []
    #처음 교실의 끝나는 시간 추가
    heapq.heappush(room, times[0][1])
    
    for i in range(1, len(times)):
        #이전 수업의 끝나는 시간 <= 현재 수업의 시작 시작
        if room[0] <= times[i][0]:
            #끝나는 시간을 업데이트
            heapq.heappop(room)
            heapq.heappush(room, times[i][1])
        else:
            #끝나는 시간을 추가
            heapq.heappush(room, times[i][1])
               
    return len(room)

def main() :
    #강의실의 개수
    n = int(input())
    
    #시작 시간, 끝 시간
    times = [list(map(int, input().split())) for _ in range(n)]
    times.sort()
        
    print(classroom(times))
   
if __name__ == "__main__" : 
    main()