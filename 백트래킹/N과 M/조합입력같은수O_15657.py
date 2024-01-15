import sys
input = sys.stdin.readline

def combination_input_same_number_possible(vlist, index):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(index, n):
        combination_input_same_number_possible(vlist + [input_list[i]], i)

if __name__ == "__main__":
    index = 0
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()
    combination_input_same_number_possible(vlist, index)