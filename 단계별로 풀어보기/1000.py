import sys 
input = sys.stdin.readline

def sum(a, b) :
    result = a + b
    return result

if __name__ == "__main__" :
    a, b = map(int, input().split())
    print(sum(a, b))