class Search:
    def interpolation_search(self, nums, target, left= 0, right= None):
        if right is None:
            right = len(nums) - 1 
        
        if left > right or nums[left] > target or nums[right] < target:
            return -1

        mid = left + int((((target - nums[left]) * (right - left)) / (nums[right] - nums[left])))
        if mid >= len(nums):
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.interpolation_search(nums, target, mid + 1, right)
        else: 
            return self.interpolation_search(nums, target, left, mid - 1)

    
nums = input("Enter Elements seperated by ' ' : ")
target = int(input("Enter the number you want to search: "))
nums = nums.split()
nums = [int(num) for num in nums]

search = Search()
ind = search.interpolation_search(nums, target)
print(ind)