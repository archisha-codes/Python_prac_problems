# BRUTE FORCE USING BUBBLE SORT
def bubble_sort(n):
    length = len(n)

    for i in range(length - 1):
        for j in range(length - i - 1):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]


# Test the function
if __name__ == "__main__":
    n = [2, 0, 2, 1, 1, 0]
    bubble_sort(n)
    print(n)


#OPTIMIZED SOLUTION
def sortColors(nums):
    count0 = 0
    count1 = 0
    count2 = 0

    # Count occurrences
    for v in nums:
        if v == 0:
            count0 += 1
        elif v == 1:
            count1 += 1
        else:
            count2 += 1

    # Overwrite the array
    ind = 0

    while ind < count0:
        nums[ind] = 0
        ind += 1

    while ind < count0 + count1:
        nums[ind] = 1
        ind += 1

    while ind < count0 + count1 + count2:
        nums[ind] = 2
        ind += 1


# ---- Test in VS Code ----
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    print(nums)
