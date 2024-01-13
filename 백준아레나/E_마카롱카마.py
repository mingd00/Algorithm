import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def pelindrom(n, copy_arr, values):
    for i in range(n//2):
        if copy_arr[i] == copy_arr[n-i-1]:
            continue
        else:
            return
    s = ''
    for i in copy_arr:
        s += i
    values.append(s)
    return
        
        
def macaron(start, n, arr, copy_arr, values):
    for k in range(max(arr)):
        for i in range(start, max(arr)):
            if arr[k] > arr[i]:
                copy_arr[k] == arr[k] 
                pelindrom(n, copy_arr, values)
                macaron(i, n, arr, copy_arr, values)         

def main():
    n = int(input())
    size = input().rstrip()
    arr = []
    for i in range(n):
        arr.append(int(size[i]))
        
    copy_arr = copy.deepcopy(arr)
    values = ''
    macaron(0, n, arr, copy_arr, values)
    print(max(values))

if __name__ == "__main__":
    main()