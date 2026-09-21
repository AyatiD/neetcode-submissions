from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        result=[]
        left=0
        for right in range(len(nums)):
            #remove the smaller or equal elements from the back
            while dq and nums[dq[-1]]<=nums[right]:
                dq.pop()
            
            #add the new element
            dq.append(right)

            #removing the elements outside the window
            while dq and dq[0]<left:
                dq.popleft()
            
            #once window becomes k
            if right-left+1==k:
                result.append(nums[dq[0]])        
                left+=1
                
        return result