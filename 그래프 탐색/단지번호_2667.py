import sys
from collections import deque
input = sys.stdin.readline
                
def apartment_bfs(apartment, n, x, y):  
    #상하좌우
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((x, y))
    
    #시작 정점은 방문 했다고 가정
    apartment[x][y] = 0
    count = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 체크
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            
            #집이 없는 경우
            if apartment[nx][ny] == 0:
                continue
            
            #집이 있는 경우
            if apartment[nx][ny] == 1:
                apartment[nx][ny] = 0
                count += 1
                q.append((nx, ny))
                
    return count

def apartment_check():
    n = int(input())
    apartment = [list(map(int,input().rstrip())) for _ in range(n)]
    house = []
   
    #집이 모여있는 곳에서 계속 bfs 돌리고 house_count값 저장
    for i in range(n):
        for j in range(n):
            if apartment[i][j] == 1:
                house_count = apartment_bfs(apartment, n, i, j)
                house.append(house_count)
    
    house.sort()
    print(len(house))
    for i in house:
        print(i)

if __name__ == "__main__":
    apartment_check()
    

'''
문제: 단지 번호 붙이기 -> 연결되어 있는 단지 찾고 각각 단지의 집 개수 출력하기
알고리즘: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
느낀점: sys.stdin.readline은 시간 효율을 위해 씀. 하지만, 문자열을 받아올 땐 공백을 제거하는 rstrip() 해줘야 함.
        que에 append 할 때는 tuple이 더 좋음(시간 효율 증가)
        탐색 시작 위치에 유의하기(처음 시작하는 지점을 이미 탐색한 것으로 볼 것인지 탐색 대상으로 볼 것인지)
  
'''