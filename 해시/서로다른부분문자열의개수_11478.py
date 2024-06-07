import sys
input = sys.stdin.readline

def cal(x):
    rset = set()
    for i in range(len(s)):
        if x+i < len(s)+1:
            rset.add(s[i:x+i])
    return len(rset)

    
if __name__ == "__main__":
    s = input().rstrip()
    # 길이가 1일 때와 문자열 전체일 때
    res = len(set(s)) + 1
    for i in range(2, len(s)):
        res += cal(i)
    print(res)