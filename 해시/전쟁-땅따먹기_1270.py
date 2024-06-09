import sys 
input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        tdic = dict()
        tlist = list(map(int, input().split()))
        target = tlist[0]
        for i in range(1, target+1):
            if tlist[i] not in tdic:
                tdic[tlist[i]] = 0
            tdic[tlist[i]] += 1
        
        for k, v in tdic.items():
            if v > target / 2:
                print(k)
                break
        else:
            print('SYJKGW')

if __name__ == "__main__" : 
    main()