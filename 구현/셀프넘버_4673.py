import sys 
input = sys.stdin.readline

def main():
    vlist = [i+1 for i in range(10000)]
    
    for i in range(1, 10000):
        target = str(i)
        res = 0
        for t in target:
            res += int(t)
        res += i
        if res in vlist:
            vlist.remove(res)
        
    for v in vlist:
        print(v)
            

if __name__ == "__main__" : 
    main()