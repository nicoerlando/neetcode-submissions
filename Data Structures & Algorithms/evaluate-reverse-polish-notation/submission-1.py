class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        dq = deque()
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                dq.append(token)

            else:
                if token == "+":
                    res = int(dq.pop()) + int(dq.pop())

                elif token == "-":
                    operand = int(dq.pop())
                    res = int(dq.pop()) - operand

                elif token == "*":
                    res = int(dq.pop()) * int(dq.pop())

                elif token == "/":
                    operand = int(dq.pop())
                    res = int(float(dq.pop()) / operand)

                dq.append(str(res))
                    
        return int(dq.pop())


        