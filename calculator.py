import sys
from calc import add, subtract, multiply, divide, power, explanation

def get_args():
    try:
        return (sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
        print('Not all arguments have been provided')
        print('USAGE: [operation] [start_number] [operation_number]')
        raise
    except:
        print('Unknown error! See the details and usage reminder below')
        print('USAGE: [operation] [start_number] [operation_number]')
        raise

def main():
    operation, start_number, operation_number = get_args()

    #print(operation)
    #print(start_number)
    #print(operation_number)

    if operation == 'add':
        result = add(start_number, operation_number)
    elif operation == 'subtract':
        result = subtract(start_number, operation_number)
    elif operation == 'multiply':
        result = multiply(start_number, operation_number)
    elif operation == 'divide':
        result = divide(start_number, operation_number)
    elif operation == 'power':
        result = power(start_number, operation_number)
    
    print(f'The result is {result}")
    print(explanation(start_number, operation_number, operation, result))

    return 0


if __name__ == '__main__':
    sys.exit(main())