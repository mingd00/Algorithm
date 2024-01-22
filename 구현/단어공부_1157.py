import sys 
input = sys.stdin.readline

def main() :
    #대문자로 입력 받기
    n = input().rstrip().upper()
    #중복값 제거
    arr = list(set(n))
    
    count_list = []
    
    for i in arr:
        count = n.count(i)
        count_list.append(count)
    
    #count 숫자 최댓값이 중복되면    
    if count_list.count(max(count_list)) > 1:
        print('?')
    else:
        max_index = count_list.index(max(count_list))
        print(arr[max_index])   

if __name__ == "__main__" : 
    main()