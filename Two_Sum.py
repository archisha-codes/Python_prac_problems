

n=[2,7,12,15]
t=9
'''
b=0
a=len(n)
for i in range(b,a-1):
    for j in range(b+1,a-1):
        if n[b]+n[b+1]==t:
            return [n[b],n[b+1]]


'''

def twoSum(nums,target):
    x=0
    l=len(nums)
    while x<l:
        z=x+1
        while z<l:
            if nums[z]+nums[x]==target:
                return [x,z]
            z+=1
        x+=1
    return []
print(twoSum(nums=[2,7,12,15],target=9))


def twoSum(nums, target):
    index = 0
    m = {}

    for val in nums:
        res = target - val
        if res in m:
            return [m[res], index]
        m[val] = index
        index += 1

    return []

n = [2, 7, 13, 15]
print(twoSum(n, 9))

