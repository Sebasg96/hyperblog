from collections  import Counter
'''def is_armstrong_number(number):
    sum_value = 0
    number_list = [int(x) for x in str(number)]
    for element in number_list:
        sum_value += element ** len(number_list)
    return sum_value == number

    
print(is_armstrong_number(153))'''

dice_1 = [2,4,4,4,3]

sort_dice = Counter(dice_1).most_common(1)

def four_of_a_kind(dice):
    sort_dice = Counter(dice_1).most_common(1)
    return sort_dice[0][0]*4 if sort_dice[0][1] >= 4 else 0


print(four_of_a_kind(dice_1))

