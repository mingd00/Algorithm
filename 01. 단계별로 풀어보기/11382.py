import sys 
input = sys.stdin.readline

def sum(vlist) :
    global answer
    for i in vlist:
        answer += i
    return answer

if __name__ == "__main__" :
    answer = 0
    vlist = list(map(int, input().split()))
    print(sum(vlist))