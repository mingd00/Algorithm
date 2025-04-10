import sys
input = sys.stdin.readline
from itertools import combinations

def cal(words, N, K):
    if K < 5:
        return 0
    elif K ==26:
        return N
    
    max_cnt = 0
    target = [1 << i for i in range(26)]
    for i in [ord(ch) - ord('a') for ch in 'antic']:
        target.remove(1 << i)
    
    for combi in combinations(target, K-5):
        cnt = 0
        base = sum(1 << (ord(c) - ord('a')) for c in 'antic')
        
        for c in combi:
            base += c
        for w in words:
            if base & w == w:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt 

def main():
    N, K = map(int, input().split())
    words = []
    for _ in range(N):
        w = 0
        for i in list(input().rstrip()):
            # 비트마스크 형태로 변환 (알파벳을 숫자로 변환 후 해당 위치에 비트를 1로 만듦)   
            # a -> 0 -> 0b000...0001, b -> 1 -> 0b000...0010
            w |= (1 << (ord(i) - ord('a')))
        words.append(w)
    
    print(cal(words, N, K))

if __name__ == "__main__":
    main()