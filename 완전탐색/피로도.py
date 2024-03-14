from itertools import permutations

def solution(k, dungeons):
    max_count = 0 # 최대 던전 수
    permut = list(permutations(dungeons, len(dungeons)))
    
    for dungeon in permut:
        cnt = 0
        hp = k
        for d in dungeon:
            if d[0] <= hp:
                hp -= d[1]
                cnt += 1
            
        if max_count < cnt:
            max_count = cnt

    return max_count

print(solution(80, [[80,20],[50,40],[30,10]]))