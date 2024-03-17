import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    board = []
    result = []
    
    for _ in range(n):
        board.append(list(input()))    
    
    for i in range(n-7):
        for j in range(m-7):
            w_start = 0
            b_start = 0
            for a in range(i, i+8):
                for b in range(j, j+8):
                    # 합이 짝수인 칸
                    if (a+b)%2 == 0:
                        if board[a][b] == 'W':
                            b_start += 1   
                        else:
                            w_start += 1
                    # 합이 홀수인 칸
                    else:
                        if board[a][b] == 'W':
                            w_start += 1
                        else:
                            b_start += 1
            result.append(w_start)
            result.append(b_start)
    print(min(result))
                                 
if __name__ == "__main__":
    main()