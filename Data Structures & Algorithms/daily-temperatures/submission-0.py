class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]#this stores the indices exactly which indices correspond to the present one as its answer

        for i in range(len(temperatures)):

            #while stack is not empty & the now<prev
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_day=stack.pop()
                result[prev_day]=i-prev_day

            #after the loop or if the stack was empty then direct initially    
            stack.append(i)
        return result
