import sys 
input = sys.stdin.readline
from collections import deque

if __name__ == "__main__" : 
    n = int(input())
    s = deque()
    for _ in range(n):
        i = int(input())
        if i != 0:
            s.append(i)
        else:
            s.pop()
    print(sum(s))