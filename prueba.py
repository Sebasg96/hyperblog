def is_armstrong_number(number):
    sum_value = 0
    number_list = [int(x) for x in str(number)]
    for element in number_list:
        sum_value += element ** len(number_list)
    return sum_value == number

    
print(is_armstrong_number(153))
