import sys
input = sys.stdin.readline

def cal(s):
    answer = 0
    tmp = 1
    stack = []
    
    for i in range(len(s)):
        if string[i] == '(':
            stack.append('(')
            tmp *= 2
        elif string[i] == '[':
            stack.append('[')
            tmp *= 3
        elif string[i] == ')':
            if not stack or stack[-1] == '[':
                answer = 0
                break
            if string[i-1] == '(':
                answer += tmp
            stack.pop()
            tmp //= 2
        else:
            if not stack or stack[-1] == '(':
                answer = 0
                break
            if string[i-1] == '[':
                answer += tmp
            stack.pop()
            tmp //= 3
    
    if stack:
        print(0)
    else:
        print(answer)
        
if __name__ == "__main__":
    string = list(input().rstrip())
    cal(string)