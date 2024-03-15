def solution(numbers):
    answer = ''
    slist = [str(num) for num in numbers]
    sorted_slist = sorted(slist, key=lambda x: x*3, reverse=True)
    answer = ''.join(sorted_slist)
    # test case [0, 0] -> 0처리를 위해 정수형으로 변환한 후 다시 문자열로 변환
    return str(int(answer))

print(solution([0, 0]))