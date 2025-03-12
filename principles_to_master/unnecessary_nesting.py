def process_numbers(numbers):
    result=[]
    for num in numbers:
        if num < 0:
            print(f"Skipping {num}, not positive")
            continue
        if num % 2 != 0:
            print(f"Skipping {num}, not even")
            continue
        if num >= 100:
            print(f"Skipping {num}, too large")
            continue
        result.append(num)
    return result
## Using continue and removing nesting makes the code more readable and easier to understand.
## The code is also more efficient as it does not need to check the same condition multiple times.

    # old code
    for num in numbers:
        if num > 0:
            if num % 2 == 0:
                if num < 100:
                    result.append(num)
                else:
                    print(f"Skipping {num}, too large")
            else:
                print(f"Skipping {num}, not even")
        else:
            print(f"Skipping {num}, not positive")

    return result
