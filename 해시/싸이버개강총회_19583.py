import sys 
input = sys.stdin.readline

def main():
    S, E, Q = input().rstrip().split()
    chat = []
    while True:
        c = input().rstrip().split()
        if c == []:
            break
        chat.append(list(c))
    
    attend = dict()
    target = 0
    for i in range(len(chat)):
        hour, minute = chat[i][0].split(':')
        # 시작 전
        start_h, start_m = S.split(':')
        if hour < start_h or (hour == start_h and minute <= start_m):
            attend[chat[i][1]] = True
            target = i
        # 하나라도 개총 전에 입력된 채팅이 아니라면 개총이 시작된 것
        else:
            break
    
    cnt = 0    
    for i in range(target+1, len(chat)):
        hour, minute = chat[i][0].split(':')
        # 개총 끝 ~ 스트리밍 중지
        end_h, end_m = E.split(':')
        total_h, total_m = Q.split(':')
        if (hour > end_h or (hour == end_h and minute >= end_m)) and (hour < total_h or (hour == total_h and minute <= total_m)):
            # attend에 chat[i][1]가 없을 수도 있음 True인지 확인하는게 먼저가 아니라 존재 여부를 먼저 확인해야 함
            if chat[i][1] in attend:
                if attend[chat[i][1]] == True:
                    cnt += 1
                    attend[chat[i][1]] = False
                   
    print(cnt)    
        
if __name__ == "__main__" : 
    main()