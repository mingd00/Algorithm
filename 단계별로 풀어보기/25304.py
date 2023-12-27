import sys 
input = sys.stdin.readline

# 1차원 리스트 
def check_receipt_1list(total, count, info) :
    sum = 0
    for i in range(0,count*2,2) :
        sum += info[i] * info[i+1]
    if total == sum :
        return "Yes"
    else :
        return "No"
    
# 2차원 리스트 
def check_receipt_2list(total, count, info) :
    sum = 0
    for i in range(count) :
        sum += info[i][0] * info[i][1]
    if total == sum :
        return "Yes"
    else :
        return "No"

# 딕셔너리 
def check_receipt_dict(total, info) :
    sum = 0
    for i in info.items():
        print(i)
        sum += i[0]*i[1]
    if total == sum :
        return "Yes"
    else :
        return "No"

if __name__ == "__main__" :
    info = []
    dic = {}
    total = int(input())
    count = int(input())
    
    # 1차원 리스트
    # for i in range(count):
    #     price, num = map(int, input().split())
    #     info.extend([price, num])
    # print(check_receipt_1list(total, count, info))

    # 2차원 리스트
    for i in range(count):
        val = list(map(int, input().split()))
        info.append(val)
    print(check_receipt_2list(total, count, info))
        
    # 딕셔너리 -> 틀림  
    # for i in range(count):
    #     key = list(map(int, input().split()))
    #     dic[key[0]] = key[1]
    # print(check_receipt_dict(total, dic))

