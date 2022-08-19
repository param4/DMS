class Search:
    def ternary_search(self, nums, target, left= 0, right= None):
        if right is None:
            right= len(nums)-1
        interval = (right - left) // 2
        mid1 = left + interval
        mid2 = right - interval

        if left > right:
            return -1
        if nums[mid1] == target:
            return mid1
        elif nums[mid2] == target:
            return mid2
        elif (nums[mid1] > target):
            return self.ternary_search(nums, target, left, mid1 - 1)
        elif (nums[mid2] < target):
            return self.ternary_search(nums, target, mid2 + 1, right)
        else: 
            return self.ternary_search(nums, target, mid1 + 1, mid2 - 1)

nums = input("Enter Elements seperated by ' ' : ")
target = int(input("Enter the number you want to search: "))
nums = nums.split()
nums = [int(num) for num in nums]

search = Search()
ind = search.ternary_search(nums, target)
print(ind)