def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in seen:
            
            return [seen[c], i]
        seen[num] = i
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))