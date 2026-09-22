class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        pair={
            ')':'(',
            '}':'{',
            ']':'['
            }

        for char in s:

            #for opening brackets
            if char in '({[':
                result.append(char)
            
            #for closing bracket
            else:
                #nothing in the stack to match with ie stack is empty
                if not result:
                    return False

                #if the element is NOT the matching bracket
                if result[-1]!=pair[char]:
                    return False

                #finally correct match
                result.pop()

            #valid only when the stack will be empty & its matching pairs would be removed
        return len(result)==0