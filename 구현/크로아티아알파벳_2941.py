import sys 
input = sys.stdin.readline

if __name__ == "__main__" : 
    S = input().rstrip()
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    
    for i in croatia:
        S = S.replace(i, '*')
    print(len(S))