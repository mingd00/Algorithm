import sys
input = sys.stdin.readline

def permutation_input(vlist, visited):
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            permutation_input(vlist + [sorted_list[i]], visited)
            visited[i] = 0
            
def sort_list(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

if __name__ == "__main__":
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    sorted_list = sort_list(input_list)
    visited = [ 0 for _ in range(n) ]
    permutation_input(vlist, visited)