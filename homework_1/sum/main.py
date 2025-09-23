def max_even_sum(nums: list[int]) -> int:
    if not nums:
        return 0

    total = sum(nums)
    if total % 2 == 0:
        return total

    min_odd = min([x for x in nums if x % 2 == 1])
    return total - min_odd


def main():
    nums = list(map(int, input().split()))
    result = max_even_sum(nums=nums)
    print(result)
    return result


if __name__ == "__main__":
    main()
