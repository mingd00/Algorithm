import sys
input = sys.stdin.readline

def permutation_same_number_possible_input(vlist):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        permutation_same_number_possible_input(vlist + [sorted_list[i]])

def sort_list(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

if __name__ == "__main__":
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    sorted_list = sort_list(input_list)
    permutation_same_number_possible_input(vlist)