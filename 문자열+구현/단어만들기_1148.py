import sys
input = sys.stdin.readline
from collections import Counter

# puzzle에 글자가 포함되는지 체크
def check(word_counter, puzzle_counter):
    for char, cnt in word_counter.items():
        if cnt > puzzle_counter.get(char, 0):
            return False
    return True

# [(글자, Counter 객체), ...] 반환
def preprocess_dict(dic):
    return [(word, Counter(word)) for word in dic]

if __name__ == "__main__":
    dic, puzzle = [], []
    while True:
        v = input().rstrip()
        if v == '-':
            break
        dic.append(v)
    while True:
        v = input().rstrip()
        if v == '#':
            break
        puzzle.append(list(v))
    
    dic = preprocess_dict(dic)
            
    for p in puzzle:
        min_max = []
        puzzle_counter = Counter(p)
        target_p = list(set(p)) # 중복값 제거
        
        # 퍼즐에서 가운데에 올 수 있는 모든 글자 탐색
        for char in target_p:
            cnt = 0
            for word, word_counter in dic:
                if char in word and check(word_counter, puzzle_counter):
                    cnt += 1
            min_max.append((cnt, char))

        # 최소, 최대 찾기
        min_max.sort()
        min_res, max_res = [], []
        min_cnt = min_max[0][0]
        max_cnt = min_max[-1][0]
        
        for cnt, char in min_max:
            if cnt == min_cnt:
                min_res.append(char)
            if cnt == max_cnt:
                max_res.append(char)
        
        min_res = ''.join(sorted(min_res))
        max_res = ''.join(sorted(max_res))
        
        print(min_res, min_cnt, max_res, max_cnt)
                
            
                
        
        