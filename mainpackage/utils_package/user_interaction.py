from ..math_package import *
def user_interaction():
    inp = input(f'''Which operation do you want to use? Please enter the ID of the action. Enter "-1" to exit.
Possible actions:
1. square
''')
    try:
        act_id = int(inp)
    except:
        print('This is not a valid ID.')
        inp = input(f'''Which operation do you want to use? Please enter the ID of the action. Enter "-1" to exit.
Possible actions:
1. square
''')
        act_id = int(inp)

    while act_id != -1:
        if act_id == 1:
            try:
                x = int(input('Please enter x:\n'))
            except:
                print('This is not a valid number.')
                x = int(input('Please enter x:'))

            print(f'result: {square(x)}')

        #######

        inp = input(f'''Which operation do you want to use? Please enter the ID of the action. Enter "-1" to exit.
Possible actions:
1. square
''')
        act_id = int(inp)

