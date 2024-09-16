#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n): #Repetition will be avoided
            if nums[i] +nums[j]==target:
                return [i,j]
            
        return "Index not found"

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))


#Output: [0,1]
