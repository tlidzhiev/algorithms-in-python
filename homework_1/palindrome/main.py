def is_palindrome(n: int) -> bool:
    if n < 0:
        return False

    if n != 0 and n % 10 == 0:
        return False

    rev: int = 0
    x: int = n
    while x > 0:
        rev = rev * 10 + (x % 10)
        x //= 10

    return rev == n


def main():
    n = int(input())
    result = is_palindrome(n=n)
    print(result)
    return result


if __name__ == "__main__":
    main()
