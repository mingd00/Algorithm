import sys
input = sys.stdin.readline

def combination_input(vlist, index):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(index, n):
        combination_input(vlist + [sorted_list[i]], i)

def sort_list(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

if __name__ == "__main__":
    index = 0
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    sorted_list = sort_list(input_list)
    combination_input(vlist, index)