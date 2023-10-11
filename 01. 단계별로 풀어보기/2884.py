import sys 
input = sys.stdin.readline

def timer(h,m) :
    if m >= 45 :
        m -= 45
    else : 
        h -= 1
        m = 60-(45-m)
        if h < 0 :
            h = 23
    result = str(h)+" "+str(m)
    return result

if __name__ == "__main__" :
    h,m = map(int, input().split())
    print(timer(h,m))