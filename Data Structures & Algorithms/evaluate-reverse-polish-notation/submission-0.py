class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()

                if token=="+":
                    result=int(a+b)
                elif token=="-":
                    result=int(a-b)
                elif token=="*":
                    result=int(a*b)
                else:
                    result=int(a/b)

                stack.append(result)

        return stack[-1]