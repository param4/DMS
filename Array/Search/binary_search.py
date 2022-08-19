class Search:
    def binary_search(self, nums, target):
        return self.binary_search_helper(nums, target, 0, len(nums) - 1)

    def binary_search_helper(self, nums, target, left, right):
        if left>right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search_helper(nums, target, left + 1, right)
        else:
            return self.binary_search_helper(nums, target, left, right - 1)

nums = input("Enter Elements seperated by ' ' : ")
target = int(input("Enter the number you want to search: "))
nums = nums.split()
nums = [int(num) for num in nums]

search = Search()
ind = search.binary_search(nums, target)
print(ind)