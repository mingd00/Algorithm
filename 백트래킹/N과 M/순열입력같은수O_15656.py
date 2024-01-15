import sys
input = sys.stdin.readline

def permutation_input_same_number_possible(vlist):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        permutation_input_same_number_possible(vlist + [input_list[i]])

if __name__ == "__main__":
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()
    permutation_input_same_number_possible(vlist)