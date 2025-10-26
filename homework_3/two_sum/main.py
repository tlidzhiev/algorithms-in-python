def two_sum(arr: list[int], k: int) -> tuple[int, int]:
    seen = {}

    for i, num in enumerate(arr):
        complement = k - num

        if complement in seen:
            index1 = seen[complement]
            index2 = i
            return (min(index1, index2), max(index1, index2))

        seen[num] = i


def main():
    arr = list(map(int, input().split()))
    k = int(input())

    result = two_sum(arr, k)
    print(f"{result[0]} {result[1]}")
    return result


if __name__ == "__main__":
    main()
