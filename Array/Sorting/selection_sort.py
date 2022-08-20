class Sort: 
    def select(self, arr, i):
        min_index = i
        for ind in range(i+1, len(arr)):
            if arr[ind] < arr[min_index]:
                min_index = ind
        return min_index
    
    def selection_sort(self, arr, n= None):
        if n is None:
            n = len(arr)

        for i in range(0, n-1):
            min_index = self.select(arr, i)
            if min_index != i:
                temp= arr[min_index]
                arr[min_index]= arr[i]
                arr[i]= temp
        return arr

nums = input("Enter Elements seperated by ' ' : ")
nums = nums.split()
nums = [int(num) for num in nums]

sort = Sort()
sort.selection_sort(nums, len(nums))
print("Sorted Array is: ", nums)