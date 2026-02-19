def three_sum_closest(nums, target):
    nums.sort()
    n = len(nums)
    
    closest_sum = nums[0] + nums[1] + nums[2]
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum
    
    return closest_sum


# ---- Main Driver Code ----
if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    target = int(input("Enter target: "))
    
    result = three_sum_closest(nums, target)
    print("Closest Sum:", result)
