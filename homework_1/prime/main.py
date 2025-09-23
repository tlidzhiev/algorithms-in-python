from math import isqrt


def count_primes(n: int) -> int:
    if n <= 2:
        return 0

    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    limit = isqrt(n - 1)
    limit = isqrt(n - 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            for m in range(start, n, p):
                sieve[m] = False

    return int(sum(sieve))


def main():
    n = int(input())
    result = count_primes(n=n)
    print(result)
    return result


if __name__ == "__main__":
    main()
