import sys
input = sys.stdin.readline

def cal(passengers):
    total, max_val = 0, float('-inf')
    for passenger in passengers:
        total -= passenger[0]
        total += passenger[1]
        max_val = max(total, max_val)
    
    return max_val
        
if __name__ == "__main__":
    passengers = list(list(map(int, input().split())) for _ in range(10))
    print(cal(passengers))