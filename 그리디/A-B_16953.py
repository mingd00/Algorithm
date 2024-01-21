import sys 
input = sys.stdin.readline

def a_to_b(a, b):
    count = 1
    while(b!=a):
        count += 1
        target = b
        
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        if target == b:
            return -1
    else:
        return count
    
def main() :
    a, b = map(int, input().split())
    print(a_to_b(a, b))

if __name__ == "__main__" : 
    main()