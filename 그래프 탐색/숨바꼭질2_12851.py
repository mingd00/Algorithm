import sys 
from collections import deque
input = sys.stdin.readline

def bfs():
    global count
    global result
    
    que = deque()
    que.append(start)
    
    while que:
        v = que.popleft()
        
        #종료 조건(start가 end에 도달했을 때)
        if v == end:
            result = count_list[v]
            count += 1
            #연산이 처음부터 돌아가야 함
            continue
        
        for nv in (v-1, v+1, v*2):
            #범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문 + 1일 때 -> 동일한 탐색 횟수를 가진 곳
            if 0 <= nv <= max and (count_list[nv] == 0 or count_list[nv] == count_list[v] + 1):
                que.append(nv)   
                count_list[nv] = count_list[v] + 1
    
if __name__ == "__main__" : 
    start, end = map(int, input().split())
    max = 10 ** 5
    count, result = 0, 0
    count_list = [0 for _ in range(max+1)]
      
    bfs()
    print(result)
    print(count)
    