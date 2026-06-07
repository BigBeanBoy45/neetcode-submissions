class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        for c in s:
            
            match c:
                case '(':
                    stack.append(')')
                case '{':
                    stack.append('}')
                case '[':
                    stack.append(']')
                case ')' | '}' | ']': 
                    if len(stack) == 0 or stack[-1] is not c:
                        print(str(stack))
                        return False
                    
                    stack.pop()
            
        print("end "+ str(stack))

        if len(stack) == 0: 
            return True
        
        return False