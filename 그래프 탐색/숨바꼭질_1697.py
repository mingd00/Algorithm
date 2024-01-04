import sys
input = sys.stdin.readline
from collections import deque

def find_bfs(start, end, max, count):
    que = deque()
    que.append(start)
     
    while que:
        v = que.popleft()
        
        #탈출 조건
        if v == end:
            print(count[v])
            return
        
        #한 칸씩 이동, 순간 이동
        for nx in (v-1, v+1, v*2):
            #인덱스 범위를 벗어나지 않고, 방문하지 않은 값일 때
            if 0<=nx<=max and not count[nx]:
                count[nx] = count[v] + 1
                que.append(nx)
              
def main():
    start, end = map(int, input().split())
    max = 10**5
    count = [0] * (max+1)
    find_bfs(start, end, max, count)

if __name__ == "__main__":
    main()