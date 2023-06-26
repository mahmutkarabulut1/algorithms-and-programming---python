MIN_TAW_NUMBER = 10
MAX_DEFECT = 2

continuation = "y"                 # yes or no

all_boxes = 0                      # number of all boxes
manufacturing_defect_box = 0       # number of faulty boxes
accepted_boxes = 0                 # number of accepted boxes
number_of_taws_returned = 0        # number of returned taws
number_of_taws_accepted = 0        # number of accepted taws
all_taws_equal = 0                 # number of boxes in which all taws are equal
a_taw_heavier = 0                  # the number of boxes in which one taw is heavier than the others
a_taw_lighter = 0                  # the number of boxes in which one taw is lighter than the others
which_box = 0                      # to indicate which box it is in

sum_of_differences_for_heavier = 0  # the sum of the differences in the boxes where one taw is heavier
sum_of_differences_for_lighter = 0  # the sum of the differences in the boxes where one taw is lighter
sum_of_percentages_for_heavier = 0  # the sum of the percentages of differences in boxes where one taw is heavier than the others
sum_of_percentages_for_lighter = 0  # the sum of the percentages of differences in boxes where one taw is lighter than the others

where_heaviest_taw = 0             # to identify the box with the heaviest taws (among boxes where all taws are equal)
where_most_taws = 0                # to determine the box with the most taws (among boxes where all taws are equal)
weight_of_taw_in_most_taws = 0     # weight of a taw, identify the box with the heaviest taws (among boxes where all taws are equal)
number_of_taw_in_heaviest_taw = 0  # number of taws, determine the box with the most taws (among boxes where all taws are equal)

max_difference = 0
min_difference = 10000000000       # (10000000000 mg = 10 ton, a taw is on average 7000 mg, it is impossible for a marble to weigh 10 tons.)
percentage_of_max_difference = 0
percentage_of_min_difference = 0

sign1 = "+"
sign2 = "+"

different_taw = 0

while continuation == "Y" or continuation == "y":
    all_boxes += 1
    which_box += 1
    print(f"{which_box}. box")
    defect = 0
    which_taw = 3

    number_of_taws = int(input("Enter number of taws: "))
    while number_of_taws < MIN_TAW_NUMBER:
        number_of_taws = int(input("Please, enter a number greater than 10: "))

    print("1. taw ")
    first_taw = float(input("Weight of taw: "))
    print("2. taw ")
    second_taw = float(input("Weight of taw: "))
    print("3. taw ")
    third_taw = float(input("Weight of taw: "))

    if first_taw == second_taw and first_taw == third_taw:
        main_weight = first_taw
    elif first_taw == second_taw and first_taw != third_taw:
        defect += 1
        main_weight = first_taw
        different_taw = third_taw
    elif first_taw == third_taw and first_taw != second_taw:
        defect += 1
        main_weight = first_taw
        different_taw = second_taw
    elif third_taw == second_taw and first_taw != second_taw:
        defect += 1
        main_weight = second_taw
        different_taw = first_taw
    else:
        defect += 2
        main_weight = first_taw

    for taw in range(number_of_taws - 3):

        if defect >= MAX_DEFECT:
            print("Manufacturing defect")
            manufacturing_defect_box += 1
            number_of_taws_returned += number_of_taws
            break
        which_taw += 1
        print(f"{which_taw}. taw ")
        weight_of_taw = int(input("Weight of taw: "))
        if main_weight != weight_of_taw:
            defect += 1
            different_taw = weight_of_taw

    if defect < MAX_DEFECT:
        accepted_boxes += 1
        number_of_taws_accepted += number_of_taws

    if defect == 0:
        all_taws_equal += 1
        while where_heaviest_taw < main_weight:
            where_heaviest_taw = main_weight
            number_of_taw_in_heaviest_taw = number_of_taws
        while where_most_taws < number_of_taws:
            where_most_taws = number_of_taws
            weight_of_taw_in_most_taws = main_weight

    elif defect == 1:
        if main_weight < different_taw:
            a_taw_heavier += 1
            difference = different_taw - main_weight
            percentage_of_difference = difference*100/main_weight
            sum_of_differences_for_heavier += difference
            sum_of_percentages_for_heavier += percentage_of_difference
            while difference > max_difference:
                max_difference = difference
                percentage_of_max_difference = max_difference*100/main_weight
                sign1 = "+"
            while min_difference > difference:
                min_difference = difference
                percentage_of_min_difference = min_difference * 100/main_weight
                sign2 = "+"
        elif main_weight > different_taw:
            a_taw_lighter += 1
            difference = main_weight - different_taw
            percentage_of_difference = difference * 100 / main_weight
            sum_of_differences_for_lighter += difference
            sum_of_percentages_for_lighter += percentage_of_difference
            while difference > max_difference:
                max_difference = difference
                percentage_of_max_difference = max_difference*100/main_weight
                sign1 = "-"
            while min_difference > difference:
                min_difference = difference
                percentage_of_min_difference = min_difference * 100/main_weight
                sign2 = "-"
    defect = 0

    continuation = input("Is there another box? (For yes: Y,y /For no: N,n): ")
    while continuation != "y" and continuation != "Y" and continuation != "n" and continuation != "N":
        continuation = input("Please enter one of the Y, y, N, n: ")
        # This makes more sense because in this case the user has unlimited error right.
        # if I used "if continuation in list, and else" the user would have just one error right.
percentage_of_manufacturing_defult = manufacturing_defect_box*100/all_boxes
percentage_of_all_equal = all_taws_equal*100/accepted_boxes
percentage_of_a_taw_heavier = a_taw_heavier*100/accepted_boxes
percentage_of_a_taw_lighther = a_taw_lighter*100/accepted_boxes
average_sum_of_differences_for_heavier = sum_of_differences_for_heavier/a_taw_heavier
average_sum_of_percentages_for_heavier = sum_of_percentages_for_heavier/a_taw_heavier
average_sum_of_differences_for_lighter = sum_of_differences_for_lighter/a_taw_lighter
average_sum_of_percentages_for_lighter = sum_of_percentages_for_lighter/a_taw_lighter
print()
print()
print(f"Number of boxes with manufacturing defects and their percentage in all boxes (respectively): {manufacturing_defect_box}, {percentage_of_manufacturing_defult:.2f}%")
print(f"Number of taws returned and accepted (respectively): {number_of_taws_returned}, {number_of_taws_accepted}")
print()
print(f"Number of boxes in which all taws are of equal weight, 1 taw is heavier than the others, \nand 1 taw is lighter than the others, and their percentages in boxes without manufacturing \ndefects (respectively): {percentage_of_all_equal:.2f}%, {percentage_of_a_taw_heavier:.2f}%, {percentage_of_a_taw_lighther:.2f}%")
print()
print(f"Averages of weight difference values and weight difference percentages of the heavier \ntaws in boxes where 1 taw is heavier than the others (respectively): +{average_sum_of_differences_for_heavier:.2f}, +{average_sum_of_percentages_for_heavier:.2f}%")
print(f"Averages of weight difference values and weight difference percentages of the light taws \nin boxes where 1 taw is lighter than the others (respectively): -{average_sum_of_differences_for_lighter:.2f}, -{average_sum_of_percentages_for_lighter:.2f}%")
print()
print(f"Among the boxes in which all taws are of equal weight, the number of taws in the box \nwith the largest number of taws and the weight of 1 taw in that box (respectively): {where_most_taws}, {weight_of_taw_in_most_taws}mg")
print(f"Among the boxes in which all taws are of equal weight, the number of taws in the box \nwith the heaviest taws and the weight of 1 taw in that box: {where_heaviest_taw}mg, {number_of_taw_in_heaviest_taw}")
print()
print(f"The value, percentage, and sign (heavy or light) of the weight difference where the value \nof difference between the weight of the different taw and the weight of the other taws in \nthe box is the largest: {sign1}{max_difference}mg, {sign1}{percentage_of_max_difference:.2f}%")
print(f"The value, percentage, and sign (heavy or light) of the weight difference where the \npercentage of difference between the weight of the different taw and the weight of the \nother taws in the box is the smallest: {sign2}{min_difference}mg, {sign2}{percentage_of_min_difference:.2f}%")




























