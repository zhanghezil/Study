def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
nums = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(nums)
print("排序后的数组为：")
for i in range(len(nums)):
    print("%d" % nums[i], end=" ")
