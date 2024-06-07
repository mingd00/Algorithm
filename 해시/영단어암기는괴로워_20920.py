import sys
input = sys.stdin.readline
from collections import Counter

def english_words():
    res = []
    words_counter = Counter(words)
    for k, v in words_counter.items():
        res.append([k, v, len(k)])
    # 단어 빈도수, 단어 길이, 사전 순으로 정렬
    ans = sorted(res, key=lambda x: [-x[1], -x[2], x[0]])
    
    # 단어 길이 M 이상인 것만 출력
    for a in ans:
        if a[2] >= M:
            print(a[0])

if __name__ == "__main__":
    N, M = map(int, input().split())
    words = [input().rstrip() for _ in range(N)]
    
    english_words()