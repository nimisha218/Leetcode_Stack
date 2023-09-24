class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        parenthesis = {"]": "[", ")": "(", "}": "{"}

        for char in s:

            if char in parenthesis:

                if stack and stack[-1] == parenthesis[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False

























        # # you will be implementing stack push and pop here
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append('(')
        #     if s[i] == '[':
        #         stack.append('[')
        #     if s[i] == '{':
        #         stack.append('{')

        #     if s[i] == ')':
        #         if len(stack) == 0:
        #             return False
        #         temp = stack.pop()
        #         if temp != '(':
        #             return False
        #     if s[i] == ']':
        #         if len(stack) == 0:
        #             return False
        #         temp = stack.pop()
        #         if temp != '[':
        #             return False
        #     if s[i] == '}':
        #         if len(stack) == 0:
        #             return False
        #         temp = stack.pop()
        #         if temp != '{':
        #             return False
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
