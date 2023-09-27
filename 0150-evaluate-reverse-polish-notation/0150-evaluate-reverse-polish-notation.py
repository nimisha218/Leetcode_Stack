import math

class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                num1 = stack.pop()
                if stack:
                    num2 = stack.pop()
                else:
                    return num1
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num1 * num2
                
                else:
                    if (num1 > 0 and num2 > 0) or (num1 <=0 and num2 <= 0):
                        result = math.floor(num2/num1)
                    else:
                        result = math.ceil(num2 / num1)
                
                stack.append(result)

        return stack[-1]


        