import sys 
input = sys.stdin.readline

def group():
    count = 0
    for word in words:
        li = []
        target = ''
        for w in word:
            if w in li:
                if target != w:
                    break
                else:
                    continue
            elif w not in li:
                li.append(w)
                target = w
        else:
            count += 1
    return count   

if __name__ == "__main__" : 
    N = int(input())
    words = [input().rstrip() for _ in range(N)]
    print(group())