from itertools import permutations

def solution(numbers):
    per = set()
    num = list(numbers)
    
    # 숫자 조합 찾기
    n_list = []
    for i in range(1, len(num)+1):
        n_list += list(permutations(num, i))
        
    for i in n_list:
        per.add(int(''.join(i)))
        
    # 소수 판별
    maxv = max(per)
    prime = [False, False] + [True] * (maxv-1)
    for i in range(2, maxv+1):
        if prime[i]:
            for j in range(2*i, maxv+1, i):
                prime[j] = False
    
    answer = []
    for i in per:
        if prime[i]:
            answer.append(i)
            
    return len(answer)
    
print(solution('12345'))