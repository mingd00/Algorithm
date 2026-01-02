import sys

input = sys.stdin.readline


def cal(orders):
    global s
    if len(orders) == 1:
        order = orders[0]
        if order == "all":
            s = set([i for i in range(1, 21)])
        elif order == "empty":
            s = set()
    else:
        order, target = orders
        target = int(target)
        if order == "add":
            s.add(target)
        elif order == "remove":
            s.discard(target)
        elif order == "check":
            print(1) if target in s else print(0)
        elif order == "toggle":
            s.discard(target) if target in s else s.add(target)


if __name__ == "__main__":
    m = int(input())
    s = set()
    for _ in range(m):
        orders = input().rstrip().split()
        cal(orders)
