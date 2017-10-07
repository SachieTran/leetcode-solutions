class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operand_stack = []
        for token in tokens:
            print operand_stack
            if token in "*+/-":
                op2 = operand_stack.pop()
                op1 = operand_stack.pop()
                if token=='+':
                    operand_stack.append(op1+op2)
                elif token=='-':
                    operand_stack.append(op1-op2)
                elif token=='/':
                    if op2<0:
                        if op1>(-1*op2):
                            operand_stack.append(-1*(op1/(-1*op2)))
                        else:    
                            operand_stack.append(0)
                    else:    
                        operand_stack.append(op1/op2)
                elif token=='*':
                    operand_stack.append(op1*op2)
            else:
                operand_stack.append(int(token))
        
        return operand_stack.pop()

s = Solution()
input = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print s.evalRPN(input)