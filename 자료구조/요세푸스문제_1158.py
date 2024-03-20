import sys 
input = sys.stdin.readline

def main() :
    N, K = map(int, input().split())
    vlist = [i for i in range(1, N+1)]
    result = []
    num = 0
    
    for n in range(N):
        num += K-1
        if num >= len(vlist):
            num %= len(vlist)
        result.append(str(vlist.pop(num)))
                
    print("<",", ".join(result),">", sep='')
    
if __name__ == "__main__" : 
    main()