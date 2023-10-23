import sys 
input = sys.stdin.readline

def long(n) :
    for _ in range(n//4):
        string.append('long')
    string.append('int')
    return string

if __name__ == "__main__" :
    string = []
    n = int(input()) 
    print(*long(n))