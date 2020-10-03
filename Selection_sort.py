def sort(nums):
    for i in range (len(nums)-1):
        minpos = i
        for j in range (i,len(nums)):
            if  nums[j] < nums[minpos]:
                minpos=j
            
        nums[minpos],nums[i] = nums[i],nums[minpos]

        

nums = [32,61,78,34,19,12,45,55]
sort(nums)
print(nums)