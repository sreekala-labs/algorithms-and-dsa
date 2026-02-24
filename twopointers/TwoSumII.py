#Given an array of integers numbers that is sorted in non-decreasing order.
#Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
#There will always be exactly one valid solution.
#Your solution must use O(1) additional space.

#Example: Input: numbers = [1,2,3,4], target = 3
#Output: [1,2]

class TwoSum2:
    
    def indicesOfTwoSum(self, arr, target):
        i=0
        j=len(arr)-1
        
        while(i<j):
            print(arr[i])
            if arr[i] + arr[j] < target:
                i+=1
            elif arr[i] + arr[j] > target:
                j-=1
            elif arr[i]+arr[j]==target:
                return(i+1,j+1)
            
        return (-1,-1)

t = TwoSum2()
arr=[1,2,2,4,5]
target=4
output= t.indicesOfTwoSum(arr, target)
print(output)
    