MIN_ARCHER = 8

num_of_shots = int(input("Enter number of shots: "))
num_of_archer = int(input("Enter number of archer: "))
while num_of_archer < MIN_ARCHER:
    num_of_archer = int(input("Enter number of archer: "))
ranks_of_archers = [0] * num_of_archer
copy_total_points = [0] * num_of_archer

def main():
    names_of_archers = []
    total_points = [0] * num_of_archer
    num_of_10 = [0] * num_of_archer
    num_of_X = [0] * num_of_archer

    datas(total_points, num_of_10, num_of_X, names_of_archers)
    ranks(copy_total_points, ranks_of_archers, names_of_archers, total_points, num_of_10, num_of_X, num_of_archer)

def datas(total_points,num_of_10,num_of_X,names_of_archers):
    for shot in range(num_of_shots):
        for archer in range(num_of_archer):
            name = input("Enter the name of archer: ")
            names_of_archers.append(name)
            is_there_shot = input("Did the archer shot the target? (y,Y,n,N): ")
            if is_there_shot in ["y","Y"]:
                point = int(input("Enter point of archer: "))
                while point not in [10, 9, 8, 7, 6, 5]:
                    point = int(input("Enter point of archer {10,9,8,7,6,5}: "))
            else:
                point = 0

            total_points[archer] += point
            copy_total_points[archer] += point
            if point == 10:
                num_of_10[archer] += 1
                is_it_X = input("is it X (enter y,Y,n,N): ")
                if is_it_X in ["y","Y"]:
                    num_of_X[archer] += 1

def ranks(copy_total_points,ranks_of_archers,names_of_archers,total_points,num_of_10,num_of_X,num_of_archer):
    counter = 1
    print("rank    name - surname     point    10 count      X count")
    print("----    --------------     -----    --------      -------")
    for rank in range(num_of_archer):
        max_point_index = copy_total_points.index(max(copy_total_points))
        if copy_total_points.count(max(copy_total_points)) > 1:
            max_point_index = num_of_10.index(max(num_of_10))
            if num_of_10.count(max(num_of_10)) > 1:
                max_point_index = num_of_X.index(max(num_of_X))
        ranks_of_archers[max_point_index] += counter

        max_point = copy_total_points[max_point_index]
        copy_total_points.pop(max_point_index)
        max_10_point = num_of_10[max_point_index]
        num_of_10.pop(max_point_index)
        max_X_point = num_of_X[max_point_index]
        num_of_X.pop(max_point_index)
        max_archer_point = names_of_archers[max_point_index]
        names_of_archers.pop(max_point_index)
        counter += 1

        print(f"{rank + 1:2d}", end="   ")
        print(f"   {max_archer_point}",end="   ")
        print(f"{max_point:18d}",end="   ")
        print(f"{max_10_point:8d}",end="   ")
        print(f"{max_X_point:9d}",end="   ")
        print()
# sometimes shape slips a bit, but it's understandable
main()
