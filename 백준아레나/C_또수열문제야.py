import sys 
input = sys.stdin.readline

def main() :
    n = int(input())
    answer = []
    j = 0
    for i in range(0, 10**9):
        if len(answer) == n:
            print(*answer)
        j += 0
        if i != j and (i*j) % (i+j) != 0:
            answer.append(i)
        
if __name__ == "__main__" : 
    main()