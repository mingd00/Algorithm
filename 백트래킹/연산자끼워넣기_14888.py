import sys 
input = sys.stdin.readline
from itertools import permutations

def cal(depth, total, plus, minus, multiply, divide):
    global max_val, min_val
    
    if depth == N:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return
    
    if plus:
        cal(depth+1, total+Arr[depth], plus-1, minus, multiply, divide)
    if minus:
        cal(depth+1, total-Arr[depth], plus, minus-1, multiply, divide)
    if multiply:
        cal(depth+1, total*Arr[depth], plus, minus, multiply-1, divide)
    if divide:
        cal(depth+1, int(total/Arr[depth]), plus, minus, multiply, divide-1)
    
                
if __name__ == "__main__" : 
    N = int(input())
    Arr = list(map(int, input().split()))
    Operator = list(map(int, input().split()))
    
    max_val, min_val = float('-inf'), float('inf')
    cal(1, Arr[0], Operator[0], Operator[1], Operator[2], Operator[3])
    
    print(max_val)
    print(min_val)