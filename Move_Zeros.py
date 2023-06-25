def moveZeros(nums):
    n = len(nums)
    countzero = 0
    for i in range(n):
        if nums[i] != 0:
            nums[countzero] = nums[i]
            countzero += 1

    while countzero < n:
        nums[countzero] = 0
        countzero += 1

nums = [0, 1, 0, 3, 12]
nums2 = [0]
moveZeros(nums)
moveZeros(nums2)
print(nums2)
print(nums)