def advance_by(dice_input):
    if dice_input <=0:
        raise ValueError('provide number > 0')
    elif dice_input > 6:
        raise ValueError('provide number < 6')
    else:
        print(str(dice_input))

try:
    advance_by(7)
except ValueError:
    print('number must be >0 and < 6')

# if you want to display the same exception message of raisng error time.
try:
    advance_by(0)
except ValueError as err:
    print(str(err))