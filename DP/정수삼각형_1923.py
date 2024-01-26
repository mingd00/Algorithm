import sys 
input = sys.stdin.readline

def sum():
    for i in range(1, n):
        for j in range(i+1):
            #중간, 오른쪽 위 대각선과 왼쪽 위 대각선 중 더 큰 값과 합하기
            if 0 < j < i:
                vlist[i][j] = vlist[i][j] + max(vlist[i-1][j-1], vlist[i-1][j])
            #가장 왼쪽, 오른쪽 위 대각선 값과 합하기
            elif j == 0:
                vlist[i][j] = vlist[i][j]+vlist[i-1][j]
            #가장 오른쪽, 왼쪽 위 대각선 값과 합하기
            elif j == i:
                vlist[i][j] = vlist[i][j]+vlist[i-1][j-1]
            else:
                continue

if __name__ == "__main__" : 
    n = int(input())
    vlist = []
    for i in range(n):
        vlist.append(list(map(int, input().split())))
    
    sum()
    print(max(vlist[n-1]))
        