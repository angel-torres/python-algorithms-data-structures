'''
You are given an array and an element. Remove all elements in the array that have the same value as the element. 
'''

class Solution:
    def removeElement(self, nums, val):
           j = 0
    
           for i in range(len(nums)):
               if nums[i] != val:
                   nums[i],nums[j]=nums[j],nums[i]
                   j = j+1
                
           return j


newSolution = Solution()

array1 = [1,2,2,3]
element1 = 2

newSolution.removeElement(array1, element1)



