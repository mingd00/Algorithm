import sys
input = sys.stdin.readline

def backtracking(start, chicken, home, chicken_arr, M, num_of_chicken, distance):
    if len(chicken_arr) == M:
        count = 0
        for h in home:
            d = float('inf')
            for c in chicken_arr:       
                if abs(h[0] - c[0]) + abs(h[1] - c[1]) < d:
                    d = abs(h[0] - c[0]) + abs(h[1] - c[1])
            count += d
        distance.append(count)

        return
    
    for i in range(start, num_of_chicken):
        chicken_arr.append(chicken[i])
        backtracking(i+1, chicken, home, chicken_arr, M, num_of_chicken, distance)
        chicken_arr.pop()
        
def main():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    # 2(치킨집)의 좌표 저장
    chicken = []
    # 1(집)의 좌표 저장
    home = []
    
    chicken_arr = []
    distance = []
    
    for i in range(N):
        for j in range(N):
            if graph[j][i] == 2:
                chicken.append((i, j))
            elif graph[j][i] == 1:
                home.append((i, j))
            else:
                continue
                             
    backtracking(0, chicken, home, chicken_arr, M, len(chicken), distance)
    
    print(min(distance))

if __name__ =="__main__":
    main()