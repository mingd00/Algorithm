import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    words = [input().split() for _ in range(n)]
    shortcuts = []
    answer = []
    
    for word in words:
        # 단어의 첫 글자 체크
        for i in range(len(word)):
            if word[i][0].upper() not in shortcuts:
                shortcuts.append(word[i][0].upper())
                word[i] = '[' + word[i][0] + ']' + word[i][1:]
                print(*word)
                break
        # 단어의 첫 글자를 단축키로 지정 못 하는 경우 -> 왼쪽부터 탐색
        else:
            for i in range(len(word)):
                # 단축키 사용 유무 체크
                flag = False
                for j in range(1, len(word[i])):
                    if word[i][j].upper() not in shortcuts:
                        shortcuts.append(word[i][j].upper())
                        word[i] = word[i][:j] + '[' + word[i][j] + ']' + word[i][j+1:]
                        flag = True
                        print(*word)
                        break
                if flag:
                    break
            else:
                print(*word)
                
            
        
