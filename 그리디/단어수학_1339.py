import sys 
input = sys.stdin.readline

def calculate(slist):
    digit_dic = {}
    
    #자릿수를 딕셔너리에 저장 
    for word in slist:
        digit = len(word) - 1
        for current_word in word:
            if current_word in digit_dic:
                digit_dic[current_word] += pow(10, digit)
            else:
                digit_dic[current_word] = pow(10, digit)
            
            digit -= 1
            
    #딕셔너리의 값을 내림차순 정렬
    value = sorted(digit_dic.values(), reverse=True)

    result, num = 0, 9
    for v in value:
        result += v * num
        num -= 1
        
    return result

def main() :
    n = int(input())
    slist = [input().rstrip() for _ in range(n)]
    print(calculate(slist))

if __name__ == "__main__" : 
    main()