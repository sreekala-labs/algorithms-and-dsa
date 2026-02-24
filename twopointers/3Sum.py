'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5'''

class Solution:
    def threeSum(self,nums):
        #1. You need a result which has to be an array. 
        res=[]
        
        #2. Sorting the array is easier since we are returning the values and not the indices. 
        nums.sort()
        
        #using the 2 pointer approach (2sum), we have to solve this problem. 
        for i, a in enumerate(nums):
            if a > 0:
                print("a",a)
                break

            #Two pointers, j and k or left and right.
            if i > 0 and a==nums[i-1]:
                print("a","nums[i]",a,nums[i-1])
                #print("Here", i, i-1, nums[i], nums[i-1])
                continue
            left, right = i+1, len(nums)-1
            
            #Using the tecniqie of 2 pointers.
            while left < right:
                if a + nums[left] + nums[right] > 0:
                    right-=1
                elif a + nums[left] + nums[right] < 0:
                    left+=1
                else:
                    res.append([a,nums[left],nums[right]])
                    left+=1
                    right-=1    
                    while nums[left] == nums[left - 1] and left < right:
                        left+=1
        return res    
                
                
            

s= Solution()
print(s.threeSum([-3,3,4,-3,1,2]))
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,1,1]))
    
    