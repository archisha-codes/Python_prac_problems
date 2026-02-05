#from pyparsing import nums


def majorityElement(self, nums):
    cand1 = cand2 = None
    count1 = count2 = 0

    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Step 2: Verify candidates
    result = []
    limit = len(nums) // 3

    if nums.count(cand1) > limit:
        result.append(cand1)

    if cand2 != cand1 and nums.count(cand2) > limit:
        result.append(cand2)

    return result