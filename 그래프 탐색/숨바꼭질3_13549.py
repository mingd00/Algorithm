import sys 
from collections import deque
input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(start)
    
    while que:
        v = que.popleft()
        
        if v == end:
            print(count_list[v])
            return
            
        for nv in (v-1, v+1, v*2):
            if 0 <= nv <= max and not visited[nv]:
                visited[nv] = 1
                #순간이동은 0초 소요, 걷기는 1초 소요
                if nv == v*2:
                    #순간이동을 먼저해서 시간 효율 향상
                    que.appendleft(nv)
                    count_list[nv] = count_list[v]
                else:
                    que.append(nv)
                    count_list[nv] = count_list[v] + 1

if __name__ == "__main__" : 
    start, end = map(int, input().split())
    max = 10 ** 5
    visited = [0 for _ in range(max+1)]
    count_list = [0 for _ in range(max+1)]
    bfs()