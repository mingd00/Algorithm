import sys
input = sys.stdin.readline

word = input().rstrip()
tmp = []
answer = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        tmp.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])
        
print(sorted(tmp)[0])

