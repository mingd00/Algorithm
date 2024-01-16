import sys
input = sys.stdin.readline

def bfs(slist, col, row, dx, dy):
    global count
    
    # 좌측 상단에서 시작 -> 같은 문자를 중복 탐색하면 안되므로 set사용
    # que = { (0,0) }
    que = set([ (0, 0, slist[0][0]) ])
    
    while que:
        x, y, key = que.pop()
        
        count = max(count, len(key))
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < row and 0 <= ny < col and slist[ny][nx] not in key:
                que.add((nx, ny, slist[ny][nx] + key))
                
def main():
    global count
    count = 1
    #상하좌우
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    col, row = map(int, input().split())
    slist = [list(input().rstrip()) for _ in range(col)]
    
    bfs(slist, col, row, dx, dy)
    print(count)
    
if __name__ == "__main__":
    main()
    