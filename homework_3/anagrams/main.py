def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for word in strs:
        sorted_word = "".join(sorted(word))

        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []

        anagram_groups[sorted_word].append(word)

    result = list(anagram_groups.values())
    return result


def main():
    strs = input().split()

    result = group_anagrams(strs)
    print(result)
    return result


if __name__ == "__main__":
    main()
