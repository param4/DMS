class Search:
    def linear_search(self, nums, target):
        target = str(target)
        for ind in range(len(nums)):
            if nums[ind] == target:
                return ind
        return -1


N = int(input("Enter Size of Array: "))
nums = input("Enter Elements seperated by ' ' : ")
target = int(input("Enter the number you want to search: "))
nums = nums.split()

search = Search()
ind = search.linear_search(nums, target)
print(ind)