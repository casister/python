# example
print('Simple calculator example')

def add(x,y):
    """ Adds two numbers"""
    return x+y

def substract(x,y):
    """ Substract two numbers"""
    return x-y

def multiply(x,y):
    """Multimply two numbers"""
    return x*y

def divide(x,y):
    """Divide two numbers"""
    return x/y

def check_if_used_has_finished():
    """
     checks that the user wanto to finishe or not
    """
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('do you want to finish (y/n):')
        if user_input == 'y':
            user_input_accepted = True
            ok_to_finish = True #redundant, but Ok
        elif user_input == 'n':
            user_input_accepted = True
            ok_to_finish = False
        else:
            print('Response must be y/n, try again')
    return ok_to_finish

def get_operation_choice():
    """ operation to be executed"""
    input_ok = False
    while not input_ok:
        print('Menu options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('-----------------')
        user_selection = input('Please make selection')
        if user_selection in ('1', '2', '3', '4'):
                input_ok = True
        else:
            print('Invalid input (must be 1-4)')
    print('-'*10)
    return user_selection

def get_numbers_from_user():
    num1 = get_integer_input('input the first number: ')
    num2 = get_integer_input('input the first number: ')
    return num1, num2

def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be integer')
        value_as_string = input(message)
    return int(value_as_string)

#======================================================================
# main
#======================================================================
finished = False
while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)

    print('result =', result)
    print('='*10)
    finished = check_if_used_has_finished()

print('-'*20)
print('b y e')