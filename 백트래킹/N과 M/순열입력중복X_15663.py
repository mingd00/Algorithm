import sys
input = sys.stdin.readline

def permutation_input_unduplicated(vlist):
    global answer
    if len(vlist) == m:
        answer.append(vlist)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            permutation_input_unduplicated(vlist + [input_list[i]])
            visited[i] = 0

if __name__ == "__main__":
    answer = []
    vlist = []
    n, m = map(int, input().split())
    input_list = list(map(int,input().split()))
    input_list.sort()
    visited = [ 0 for _ in range(n) ]
    permutation_input_unduplicated(vlist)
    set_of_tuple = sorted(list(set(map(tuple, answer))))
    for i in set_of_tuple:
        print(*i)