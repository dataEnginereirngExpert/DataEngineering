# this program is for user defiend function 

#user  defiend function  with output 

def oddeventest(number1):
    if number1 % 2 == 0 :
        print(f" {number1} is Even ")
    else:
        print(f" {number1} is Odd ")

oddeventest(8)
oddeventest(11)

#user  defiend function  with return statement
def oddeventest_withreturn(number1):
    if number1 % 2 == 0 :
        return 'Even'
    else:
        return 'Odd'
isOddEven=oddeventest_withreturn(10)
print(isOddEven)


