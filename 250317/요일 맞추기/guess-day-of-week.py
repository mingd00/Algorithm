m1, d1, m2, d2 = map(int, input().split())

dic = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = {0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}

def cal_date(m, d):
    date = 0
    for i in range(1, m):
        date += dic[i]
    date += d
    return date

d = cal_date(m2, d2) - cal_date(m1, d1)

while d < 0:
    d += 7

print(week[(1+d) % 7])

        





