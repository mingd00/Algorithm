def solution(n, lost, reserve): 
    # 여벌이 있는 학생이 체육복을 도난 당했을 때
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    return n-len(set_lost)

print(solution(5, [2, 4], [1, 3, 5]))