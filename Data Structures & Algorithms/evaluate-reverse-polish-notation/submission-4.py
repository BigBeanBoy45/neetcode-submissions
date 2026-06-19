class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res: int = 0
        stack: List[int] = []

        for t in tokens:

            try:
                stack.append(int(t))
            except:
                top: int = stack.pop()
                if t == '+':
                    stack.append(stack.pop() + top)

                elif t == '-':
                    stack.append(stack.pop() - top)

                elif t == '*':
                    stack.append(stack.pop() * top)

                else:
                    stack.append(int(stack.pop() / top))

            print(t + " \t\t " + str(stack))
        
        return stack.pop()