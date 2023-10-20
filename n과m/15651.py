import sys 
input = sys.stdin.readline

def permutation_same_number_possible(vlist) :
    if len(vlist) == m:
        print(*vlist)
        return
    
    for i in range(n):
        permutation_same_number_possible(vlist + [i+1])

if __name__ == "__main__" :
    vlist = []
    n, m = map(int, input().split())
    permutation_same_number_possible(vlist)