import sys
input = sys.stdin.readline
from itertools import combinations

def find(nums):
    target_lst = list(combinations(nums, 7))
    for target in target_lst:
        if sum(target) == 100:
            for n in sorted(target):
                print(n)
            return 

if __name__ == "__main__":
    heights = [int(input()) for _ in range(9)]
    find(heights)