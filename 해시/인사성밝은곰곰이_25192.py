import sys 
input = sys.stdin.readline

def main():
    n = int(input())
    people = set()
    cnt = 0
    for _ in range(n):
        chat = input().rstrip()   
        if chat != 'ENTER' and chat not in people:
            people.add(chat)
            cnt += 1
        elif chat == 'ENTER':
            people = set()
    print(cnt)    

if __name__ == "__main__" : 
    main()