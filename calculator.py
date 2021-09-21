from pprint import pprint


def get_operands(eq, operator):
    operands = eq.split(operator)
    if not operands[0].strip().isnumeric() or not operands[1].strip().isnumeric():
        raise Exception('Invalid operands')
    operand1_int = int(operands[0])
    operand2_int = int(operands[1])
    return operand1_int, operand2_int


while (eq := input('Enter an equation: ')) != 'q':
    try:
        result = None
        error = None
        if eq.find('.') >= 0:
            raise Exception('Invalid operands')
        elif eq.find('+') >= 0:
            op1, op2 = get_operands(eq, '+')
            result = op1 + op2
        elif eq.find('-') >= 0:
            op1, op2 = get_operands(eq, '-')
            result = op1 - op2
        elif eq.find('*') >= 0:
            op1, op2 = get_operands(eq, '*')
            result = op1 * op2
        elif eq.find('/') >= 0:
            op1, op2 = get_operands(eq, '/')
            if op2 <= 0:
                raise Exception('Can\'t divide by 0')
            else:
                result = op1 / op2
        else:
            raise Exception('Invalid operator')
        if result is not None:
            print('Result:', '{:.2f}'.format(result))
    except Exception as e:
        print(e)
