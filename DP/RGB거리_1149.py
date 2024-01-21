import sys 
input = sys.stdin.readline

def cal_min(n, colors):
    for i in range(1, n):
        #현재 색을 제외하고 전 값들과 비교해 최솟값을 더해주기
        colors[i][0] += min(colors[i-1][1], colors[i-1][2])
        colors[i][1] += min(colors[i-1][0], colors[i-1][2])
        colors[i][2] += min(colors[i-1][0], colors[i-1][1])
        
    return min(colors[n-1])

def main() :
    n = int(input())
    colors = [list(map(int, input().split())) for _ in range(n)]
    print(cal_min(n, colors))

if __name__ == "__main__" : 
    main()