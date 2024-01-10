import sys
input = sys.stdin.readline

def backtracking(start, answer, L, C, words, vowel):
    # 모음
    vowel_count = 0
    # 자음
    consonant_count = 0
    
    if len(answer) == L:
        for i in answer:
            if i in vowel:
                vowel_count += 1
            else:
                consonant_count += 1
                
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(answer))
            
        return
    
    for i in range(start, C):
        answer.append(words[i])
        backtracking(i+1, answer, L, C, words, vowel)
        answer.pop()
         
def main():
    # 모음
    vowel = ['a', 'e', 'i', 'o', 'u']
    # 정답
    answer = []
    # 입력
    L, C = map(int, input().split())
    words = sorted(list(input().rstrip().split()))
    
    backtracking(0, answer, L, C, words, vowel)
 
if __name__ == "__main__":
    main()