m1, d1, m2, d2 = map(int, input().split())

dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
week = {0:'Sun', 1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}
week2 = {0:'Tue', 1:'Mon', 2:'Sun', 3:'Sat', 4:'Fri', 5:'Thu', 6:'Wed'}
w = 1

date = 0
if m1 <= m2:
    for i in range(m1+1, m2+1):
        date += dic[i]
    if d1 <= d2:
        date += (d2-d1)
    else:
        date -= (d1-d2)
    print(week[((date+w) % 7)])
else:
    for i in range(m2, m1):
        date += dic[i]
    if d1 <= d2:
        date -= (d2-d1)
    else:
        date += (d1-d2)
    print(week2[((date+w) % 7)])
        





