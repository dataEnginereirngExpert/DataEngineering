
class DiceInputError(Exception):
    pass
class DiceInputLowerBoundError(Exception):
    pass
class DiceInputUpperBoundError(Exception):
    pass

#Custome exception throw 
def advance_by(dice_input):
    if dice_input <=0:
        raise DiceInputLowerBoundError('provide number > 0')
    elif dice_input > 6:
        raise DiceInputUpperBoundError('provide number < 6')
    else:
        print(str(dice_input))

try:
    advance_by(0)
except DiceInputLowerBoundError as err:
    print(str(err))




