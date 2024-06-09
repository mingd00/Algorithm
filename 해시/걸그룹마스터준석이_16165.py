import sys 
input = sys.stdin.readline

def quiz(question, type):
    if type == 1:
        print(mdic[question])
    else:
        for g in sorted(gdic[question]):
            print(g)
    
if __name__ == "__main__" : 
    gdic, mdic = dict(), dict()
    N, M = map(int, input().split())
    for _ in range(N):
        members = []
        group = input().rstrip()
        n = int(input())
        for _ in range(n):
            member = input().rstrip()
            members.append(member)
            mdic[member] = group
        gdic[group] = members
        
    for _ in range(M):
        question = input().rstrip()
        type = int(input())
        quiz(question, type)
        