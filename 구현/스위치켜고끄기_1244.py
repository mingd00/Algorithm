import sys 
input = sys.stdin.readline

def change(i):
    global status
    if status[i] == 1:
        status[i] = 0
    else: status[i] = 1

N = int(input())
status = list(map(int, input().split()))
student = int(input())
clist = [list(map(int, input().split())) for _ in range(student)]

for c in clist:
    if c[0] == 1: # 남학생
        for i in range(c[1]-1, N, c[1]):
            change(i)
    else:
        t = c[1] -1
        change(t)
        for i in range(1, N//2+1): # 여학생
            if t - i < 0 or t + i >= N:
                break
            if status[t-i] == status[t+i]:
                change(t - i)
                change(t + i)  
            else:
                break
                           
for i in range(0, N, 20):
    print(*status[i:i+20])
            
                
        