import sys 
input = sys.stdin.readline
from collections import deque

def main() :
    n = int(input())
    q = deque()
    for _ in range(n):
        order = input().split()
        if order[0] == 'push':
            q.append(order[1])
        elif order[0] == 'pop':
            if len(q) == 0:
                print(-1)
            else:       
                print(q.popleft())
        elif order[0] == 'size':
            print(len(q))
        elif order[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:       
                print(0)
        elif order[0] == 'front':
            if len(q) == 0:
                print(-1)
            else:       
                print(q[0])      
        elif order[0] == 'back':
            if len(q) == 0:
                print(-1)
            else:       
                print(q[-1])                           

if __name__ == "__main__" : 
    main()