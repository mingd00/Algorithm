import sys 
input = sys.stdin.readline

#set
def compare_set(flist, slist):
  for i in slist:
    print(1) if i in flist else print(0)

#이분 탐색
def compare_binary(n, flist, slist):
    for i in slist:
        ft, lt = 0, n-1
        isExist = False
        
        #이분 탐색 시작
        while ft <= lt:
            mid = (ft + lt) // 2
            if i == flist[mid]:
                isExist = True
                print(1)
                break
            elif i > flist[mid]:
                ft = mid + 1
            else:
                lt = mid - 1
                
        if not isExist:
            print(0)
                
def main():
  n = int(input())
  #flist = set(map(int, input().split()))
  flist = list(map(int, input().split()))
  m = int(input())
  slist = list(map(int, input().split()))
  #이분 탐색을 하기 위해서는 정렬이 필수
  flist.sort()
  
  #compare_set(flist, slist)
  compare_binary(n, flist, slist)
  
if __name__ == "__main__" : 
    main()