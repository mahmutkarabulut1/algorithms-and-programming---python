def datas(number_of_shots,number_of_archers,number_of_points,total_points,point_distribution,name_of_winds,zero_count_for_winds):
    for archer in range(number_of_archers):
        points = [0] * 11
        number_of_points.append(points)

    for point in range(number_of_shots):
        print(f"{point+1}. Shots")
        for archer in range(number_of_archers):
            print(f"{archer+1}. Archer")
            point_of_archer = int(input("Enter the point of archer: "))
            while point_of_archer not in [10,9,8,7,6,5,4,3,2,1,0]:
                point_of_archer = int(input("Enter correct the point of archer: "))
            number_of_points[archer][point_of_archer] += 1
            total_points[archer] += point_of_archer
            point_distribution[point_of_archer] += 1
            if point_of_archer == 0:
                which_wind = input("Enter to which wind: ")
                while which_wind not in name_of_winds:
                    which_wind = input("Enter correct to which wind: ")
                zero_count_for_winds[which_wind] += 1
print()
def prints(name_of_winds,point_distribution,all_number_of_shots,zero_count_for_winds,number_of_points,total_points,number_of_archers):
    print("Archer Reg No    10 P     9 P     8 P     7 P     6 P     5 P     4 P     3 P     2 P     1 P     0 P    Total Points ")
    print("-------------    -----   -----    -----  -----   -----   -----    ----   -----    -----  -----   -----  ---------------")
    for archer in range(number_of_archers):
        print(f"{archer+1:12}",end="")
        for point in range(11):
            print(f"{number_of_points[archer][10-point]:8}",end="")
        print(f"{total_points[archer]:8}")

    print(f"All Archers(%)",end="")
    for distribution in range(11):
        percentage_of_point = point_distribution[10-distribution] * 100 / all_number_of_shots
        print(f"{percentage_of_point:8.2f}",end="")
    print()
    print()
    print("Wind Name     Missed Shot Rate(%)")
    print("---------     -------------------")
    for missed in name_of_winds:
        percentage_missed = zero_count_for_winds[missed] * 100 / point_distribution[0]
        print(f"{missed:<11}{percentage_missed:>11.2f}")

def main():
    number_of_shots = int(input("Enter number of shots: "))
    number_of_archers = int(input("Enter number of archers: "))
    number_of_points = []  # I collected all number of point, which archer, how many shot
    total_points = [0] * number_of_archers
    zero_count_for_winds = {"North": 0, "Northeaster": 0, "Easterly": 0, "Southeaster": 0, "South": 0, "Southwester": 0,"Westerly": 0, "Northwester": 0}
    name_of_winds = ["North", "Northeaster", "Easterly", "Southeaster", "South", "Southwester", "Westerly","Northwester"]
    point_distribution = [0] * 11
    all_number_of_shots = number_of_shots * number_of_archers  # I found sum total number of shots.
    datas(number_of_shots, number_of_archers, number_of_points, total_points, point_distribution, name_of_winds,zero_count_for_winds)
    prints(name_of_winds, point_distribution, all_number_of_shots, zero_count_for_winds, number_of_points, total_points,number_of_archers)
main()

# If there isn't any zero point shot, ZeroDivisionError might appear.


