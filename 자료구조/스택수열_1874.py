import sys 
import sys 
input = sys.stdin.readline

def main() :
    n = int(input())
    slist = [int(input()) for _ in range(n)]
    stack = []
    result = []
    
    start = 0
    for target in slist:
        while start < target:
            start += 1
            stack.append(start)
            result.append('+')
            
        if stack.pop() == target:
            result.append('-')
        else:
            print('NO')
            return
    
    for i in result:
        print(i)
            
if __name__ == "__main__" : 
    main()