class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = ["+", "-", "*", "/"]
        stack =[]
        res = 0
        for t in tokens:
            if t in opr:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    stack.append(b+a)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack[0]
