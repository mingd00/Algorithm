import sys 
input = sys.stdin.readline

def main() :
    s1 = list(input().rstrip())
    s2 = []
    n = int(input())
    orders = [input().rstrip().split() for _ in range(n)]
    
    for order in orders:
        if order[0] == 'L':
            if s1:
                s2.append(s1.pop())
        elif order[0] == 'D':
            if s2:
                s1.append(s2.pop())
        elif order[0] == 'B':
            if s1:
                s1.pop()
        elif order[0] == 'P':
            s1.append(order[1])
            
    s1.extend(reversed(s2))
    print(''.join(s1))

if __name__ == "__main__" : 
    main()