def solution(brown, yellow):
    answer = []
    # 일자로 배치
    if brown == (yellow+2)*2+2:
        answer = [yellow+2, 3]
    # 쌓아서 배치
    else:
        # 가로 >= 세로이고 yellow의 약수일 때 쌓을 수 있음
        for i in range(2, yellow):
            row, col = yellow//i, i
            # 가로<세로 이거나 나누어 떨어지지 않는다면 pass
            if row < col or yellow%i != 0:
                continue
            # 조건을 만족한다면 brown값을 만족하는지 확인
            if row*2 + (col+2)*2 == brown:
                answer = [row+2, col+2]
            else:
                continue
            
    return answer

print(solution(4899, 1))

