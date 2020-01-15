def postfix2infix(expression):
    operators = ['~', '^', '*', '/', '+', '-', '=']
    while len(expression) > 1:
        for symbol in range(len(expression)):
            index = symbol
            if expression[symbol][0] in operators and len(expression[symbol]) == 1:
                break
        if expression[index] != '~':
            newOperand = f'({expression[index-2]} {expression[index]} {expression[index-1]})'
            del expression[index-2:index+1]
            expression.insert(index-2, newOperand)
        else:
            newOperand = f'-{expression[index-1]}'
            del expression[index-1:index+1]
            expression.insert(index-1, newOperand)
    return expression[0][1:-1]

print(postfix2infix(input('Enter an RPN (postfix) expression to convert it to infix: ').split()))