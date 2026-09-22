class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position, speed))
        stack=[]
        cars.sort(reverse=True)#we are sorting it bc we gotta solve the cars nearest to the destination first so every car fleet can be compared with the one in front of it

        for pos, spd in cars:
            time=(target-pos)/spd

            #if new car comes & is greater than top or if list is empty
            if not stack or time>stack[-1]:
                stack.append(time)
            #else we dont do anything
        return len(stack)