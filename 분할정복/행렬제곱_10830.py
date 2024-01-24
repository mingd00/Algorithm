import sys 
input = sys.stdin.readline

#행렬의 곱셈
def matrix_mul(arr1, arr2):
    #곱셈 결과를 저장할 2차원 리스트
    result = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            mul = sum(arr1[row][i] * arr2[i][col] for i in range(n))
            result[row][col] = mul % 1000
    return result

#분할 정복
def power(n, arr):
    if n == 1:
        return arr
    #짝수
    if n % 2 == 0:
        #절반 계산
        half = power(n//2, arr)
        return matrix_mul(half, half)
    #홀수
    else:
        #n-1로 짝수로 만들어서 값 넘겨주기
        return matrix_mul(arr, power(n-1, arr))

if __name__ == "__main__" : 
    n, s = map(int, input().split())
    vlist = [list(map(int, input().split())) for _ in range(n)]
    
    ans = power(s, vlist)
    for row in ans:
        #1인 경우 위에 함수에서 나머지 연산을 수행하지 않으므로 한 번 더 1000으로 나눠주기
        #위에서 1000으로 나눠주는 이유는?? -> 오버플로 방지, 수가 너무 커지는 것을 방지!
        print(*[r % 1000 for r in row])