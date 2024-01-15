import sys
input = sys.stdin.readline

def combination_input(vlist, index):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(index, n):
            combination_input(vlist + [input_list[i]], i+1)

if __name__ == "__main__":
    vlist = []
    index = 0
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()
    combination_input(vlist, index)
    