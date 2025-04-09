import sys
import math
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return 0
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    else:
        return 1

def main():
    M = int(input())
    N = int(input())
    primes = [i for i in range(M, N+1) if is_prime(i)]
    
    if len(primes) == 0:
        print(-1)
    else:
        print(sum(primes))
        print(min(primes))

if __name__ == "__main__":
    main()