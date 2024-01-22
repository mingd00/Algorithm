import sys 
input = sys.stdin.readline

def main() :
    s = input().rstrip()
    english = 'abcdefghijklmnopqrstuvwxyz'
    
    #find() 사용
    for x in english:
        print(s.find(x), end = ' ')
    
    #for문 사용    
    # for i in english:
    #     if i in s:
    #         print(s.index(i), end = ' ')
    #     else:
    #         print(-1, end = ' ')
            

if __name__ == "__main__" : 
    main()