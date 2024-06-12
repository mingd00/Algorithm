import sys 
input = sys.stdin.readline

def check_range(target):
    if 1 <= target <= 8:
        return True
    else:
        return False
      
def move(order, row, col):
    if order == 'R':
        if check_range(row+1):
            row += 1

    elif order == 'L':
        if check_range(row-1):
            row -= 1
     
    elif order == 'B':
        if check_range(col-1):
            col -= 1

    elif order == 'T':
        if check_range(col+1):
            col += 1

    elif order == 'RT':
        if check_range(row+1) and check_range(col+1):
            row += 1
            col += 1

    elif order == 'LT':
        if check_range(row-1) and check_range(col+1):
            row -= 1
            col += 1

    elif order == 'RB':
        if check_range(row+1) and check_range(col-1):
            row += 1
            col -= 1

    else:
        if check_range(row-1) and check_range(col-1):
            row -= 1
            col -= 1
            
    return row, col

def king():
    global k_row, k_col, s_row, s_col
    for order in orders:
        nkr, nkc = move(order, k_row, k_col)
        # 킹이 이동하려는 위치에 돌이 있는지 체크
        if nkr == s_row and nkc == s_col:
            nsr, nsc = move(order, s_row, s_col)
            if nsr == s_row and nsc == s_col:
                pass
            else:
                s_row, s_col = nsr, nsc 
                k_row, k_col = nkr, nkc
        else:
            k_row, k_col = nkr, nkc
        
    print(kdic[k_row], k_col, sep='')
    print(kdic[s_row], s_col, sep='')
    
if __name__ == "__main__" : 
    kdic = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    vdic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    
    K, S, N = input().rstrip().split()
    k_row = vdic[K[0]]
    k_col = int(K[1])
    s_row = vdic[S[0]]
    s_col = int(S[1])

    orders = [input().rstrip() for _ in range(int(N))]

    king()
    
    
    
    