class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for c in s:
            if (c in list(parenthesis.values())):
                stack.append(c)
            elif (c in list(parenthesis)):
                if len(stack) == 0:
                    return False
                if (parenthesis[c] == stack[-1]):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0