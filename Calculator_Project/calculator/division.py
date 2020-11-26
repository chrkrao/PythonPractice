###################################################################
# AUTHORS NAME  : R.K.Rao Chigurupati
# CREATION DATE : 25-NOV-2020
# File Name     : division.py
# DESCRIPTION   : To create division() Methods for CALC
###################################################################

def divide():
    """
    This function divides the First Number by Second Number
    :return: Returns the resulting value after Division operation
    i.e. The Result Value is Rounded upto 5 Decimal Places
    """
    first_num = float(input("Enter the First Value : "))
    second_num = float(input("Enter the Second Value : "))
    while True:
        if second_num == 0:
            print(f"Division with Zero is NOT possible..!")
            second_num = float(input("Enter another value for Second NO: "))
        else:
            break
    result_div = first_num / second_num
    print(f"DIVISION of {first_num}/{second_num} is : {first_num/second_num:0.5f}")
    return round(result_div, 5)


def divide_2_numbers(first_num: float, second_num: float) -> float:
    """
    This function divides the First Number by Second Number
    :param:
    :param:
    :return: Returns the result of division
    i.e. First Number over Second Number and Rounded till 3 Decimal Places
    """
    result_div = first_num / second_num
    print(f"Result of Division : {first_num}/{second_num} = {result_div:0.3f} ")
    return round(result_div, 3)

