import sys 
input = sys.stdin.readline

def minecraft():
    height = 0
    for g in range(257):
        block = B
        for i in ground:
            # 현재 높이와 같거나 낮다면
            if i <= g:
                time[g] += g - i
                block -= g - i
            # 현재 높이보다 높다면
            else:
                time[g] += 2*(i -g)
                block += i - g
        # 오름차순 이므로 최소 시간이 같을 시 땅의 높이가 높은 것으로 저장
        if block >= 0 and time[g] <= time[height]:
            height = g

    return time[height], height

if __name__ == "__main__" : 
    N, M, B = map(int, input().split())
    ground = []
    for i in range(N):
        ground.extend(list(map(int, input().split())))
    # time[k]에 땅 높이가 k일 때의 시간 저장
    time = [0 for i in range(257)]
    print(*minecraft())
    
