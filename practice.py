import sys 
input = sys.stdin.readline

def dfs(start, vlist, visited_list, count):
  visited_list[start] = True
  print(start, end=' ')
  print(count)
  
  if count == 5:
    print(1)
  
  for i in vlist[start]:
    if not visited_list[i]:
      dfs(i, vlist, visited_list, count+1)
    

def main() :
    vlist = [[1], [0, 2], [1, 3], [2, 4], [3]]
    visited_list = [False] * 5
    
    dfs(0, vlist, visited_list, 1)

if __name__ == "__main__" : 
    main()