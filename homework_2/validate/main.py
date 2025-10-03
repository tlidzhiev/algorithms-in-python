def validate_stack_sequences(pushed: list[float], popped: list[str]) -> bool:
    stack = []
    pop_index = 0

    for num in pushed:
        stack.append(num)
        print(f"Pushed: {num}, Stack: {stack}")

        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            print(f"Popped: {popped[pop_index]}, Stack: {stack}")
            pop_index += 1
    return pop_index == len(popped)


def main():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_stack_sequences(pushed, popped)
    print(result)
    return result


if __name__ == "__main__":
    main()
