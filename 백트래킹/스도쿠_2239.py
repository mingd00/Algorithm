import sys
input = sys.stdin.readline

def row_check(x, num):
    for idx in range(9):
        if graph[x][idx] == num:
            return False
    return True

def col_check(y, num):
    for idx in range(9):
        if graph[idx][y] == num:
            return False
    return True

def rect_check(x, y, num):
    nx = x // 3 * 3
    ny = y // 3 * 3
    
    for i in range(3):
        for j in range(3):
            if graph[nx+i][ny+j] == num:
                return False
    return True

def dfs(index):
    if index == len(blank):
        for i in range(9):
            print(*graph[i], sep='')
        exit()
        
    for num in range(1, 10):
        x = blank[index][0]
        y = blank[index][1]
        
        if row_check(x, num) and col_check(y, num) and rect_check(x, y, num):
            graph[x][y] = num
            dfs(index + 1)
            graph[x][y] = 0  

if __name__ == "__main__":
    graph = [list(map(int, input().rstrip())) for _ in range(9)]
    blank = []

    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                blank.append((i, j))
                
    dfs(0)

