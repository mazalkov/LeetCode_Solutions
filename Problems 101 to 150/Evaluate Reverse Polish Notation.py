class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            try:
                t = int(token)
                stack.append(t)

            except ValueError:
                y = stack.pop()
                x = stack.pop()

                if token == "+":
                    stack.append(x + y)

                elif token == "-":
                    stack.append(x - y)

                elif token == "*":
                    stack.append(x * y)

                elif token == "/":
                    stack.append(int(x / y))

                else:
                    stack.append(-1)

        return stack[0]
