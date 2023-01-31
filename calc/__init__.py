def add(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def multiply(num1, num2):
    result = num1 * num2
    return result

def add(num1, num2):
    result = num1 + num2
    return result


def divide(num1, num2):
    result = num1 / num2
    return result

def power(num1, num2):
    result = num1 ** num2
    return result


def explanation (num1, num2, operation, result):
    by = ''
    if operation == 'multiply' or operation == 'divide':
        by = 'by '
    result = f'{num1} {operation} {by}{num2} equals {result}'
    return result