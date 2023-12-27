import sys 
input = sys.stdin.readline

def check_bfs(napa_cabbage, n, k):
    #상하좌우
    
    pass

def main():
    case = int(input())
    for _ in range(case):
        n, m, k = map(int, input().split())
        napa_cabbage = [list(map(int, input().split())) for _ in range(k)]
        check_bfs(napa_cabbage, n, k)


if __name__ == "__main__" :
    main()



'''
문제: 유기농 배추 -> 연결된 리스트의 개수 찾기
알고리즘: 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색
느낀점: 
'''