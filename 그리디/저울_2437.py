import sys 
input = sys.stdin.readline

def measure(scale_weight):
    target = 1
    for w in scale_weight:
        if target < w:
            break
        target += w
        
    return target
        

def main() :
    n = int(input())
    scale_weight = list(map(int, input().split()))
    scale_weight.sort()
    print(measure(scale_weight))

if __name__ == "__main__" : 
    main()