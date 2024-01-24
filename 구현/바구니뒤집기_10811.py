import sys 
input = sys.stdin.readline

def main() :
    a, b = map(int, input().split())
    nums = [i for i in range(a+1)]
    vlist = [list(map(int, input().split())) for _ in range(b)]
    
    for v in vlist:
        nums[v[0]:v[1]+1] = nums[v[0]:v[1]+1][::-1]
        
    print(*nums[1:])

if __name__ == "__main__" : 
    main()