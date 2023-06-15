from collections  import Counter
'''def is_armstrong_number(number):
    sum_value = 0
    number_list = [int(x) for x in str(number)]
    for element in number_list:
        sum_value += element ** len(number_list)
    return sum_value == number

    
print(is_armstrong_number(153))'''

dice_1 = [2,4,4,4,2]


def four_of_a_kind(dice):
    sort_dice = Counter(dice).most_common(1)
    return sort_dice[0][0]*4 if sort_dice[0][1] >= 4 else 0



def full_house(dice):
    sort_dice = Counter(dice).values()
    return sum(dice) if sorted(sort_dice, reverse=True) == [3,2] else 0


print (full_house(dice_1))
