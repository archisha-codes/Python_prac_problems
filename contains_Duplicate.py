from sympy import false

l1=[1,2,3,1,4,5]

l2=set(l1)
if len(l1)==len(l2):
    print("False")
else:
    print("True")

nums=[1,2,3,1,4,5]
def containsDuplicate(self, nums: list[int]) -> bool:
    m={}
    for _ in nums:
        if _ in m:
            return True
        m[_]=1
    return False
