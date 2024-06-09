import sys 
input = sys.stdin.readline

def main():
    tdic = dict()
    cnt = 0
    while True:
        tree = input().rstrip()
        if tree == '':
            break
        cnt += 1
        if tree not in tdic:
            tdic[tree] = 0
        tdic[tree] += 1
        
    for k, v in sorted(tdic.items()):
        per = v / cnt * 100
        print(f"{k} {per:.4f}")
        
if __name__ == "__main__" : 
    main()