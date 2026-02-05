def productExceptSelf(nums):
    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n

    # Prefix calculation
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Suffix calculation
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Final answer
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]

    return prefix, suffix, answer


# ------------ INPUT / OUTPUT ---------------
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

prefix, suffix, result = productExceptSelf(nums)

print("Prefix Array :", prefix)
print("Suffix Array :", suffix)
print("Final Output :", result)