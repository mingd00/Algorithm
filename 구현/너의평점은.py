import sys 
input = sys.stdin.readline

total = 0
cnt = 0
scores = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for _ in range(20):
    name, score, rank = input().rstrip().split()
    if rank != 'P':
        total += (float(score) * scores[rank])
        cnt += float(score)

ans = total / cnt
print(f'{ans:.6f}')