import sys
input = sys.stdin.readline
from collections import deque

def reverse_word():
    q = deque()
    ans = ''
    tmp = 0
    for i in S:
        if i == '<':
            while q:
                ans += q.pop()
            tmp = 1
            ans += '<'
        elif i == '>':
            tmp = 2
            ans += '>'
        elif i == ' ':
            while q:
                ans += q.pop()
            ans += ' '
        else:
            if tmp == 1:
                ans += i
            elif tmp == 2:
                q.append(i)
            else:
                q.append(i)
    while q:           
        ans += q.pop()
        
    return ans

if __name__ == "__main__":
    S = input().rstrip()
    print(reverse_word())
            