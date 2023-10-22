import sys
input = sys.stdin.readline

def combination_same_number_possible(vlist, index):
    if len(vlist) == m:
        answer.append(vlist)
        return
    
    for i in range(index, n):
        combination_same_number_possible(vlist + [input_list[i]], index)

if __name__ == "__main__":
    index = 0
    vlist = []
    answer = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()
    combination_same_number_possible(vlist, index)
    set_of_tuple = sorted(list(set(map(tuple, answer))))
    for i in set_of_tuple:
        print(*i)
    
    