#Total net salaries for the three groups (separately)
total_net_salary_1 = 0
total_net_salary_2 = 0
total_net_salary_3 = 0
#For the numbers of those in three separate salary clusters
number_of_low = 0
number_of_medium = 0
number_of_high = 0
more_than_fifty = 0
total_gross_salary = 0
#Total income tax amounts in different clusters
total_income_tax_1=0
total_income_tax_2=0
total_income_tax_3=0

gross_salary = int(input("Gross Salary: "))
while gross_salary > 0:
    if gross_salary <= 10000:
        net_salary = gross_salary * 0.85
        number_of_low +=1
        total_net_salary_1 += net_salary
        income_tax_1 = gross_salary - net_salary
        total_income_tax_1 +=income_tax_1
        print("Net Salary: ", net_salary, ", Income Tax: ", income_tax_1)
    elif 10000 < gross_salary < 25000:
        net_salary = gross_salary * 0.8
        number_of_medium += 1
        total_net_salary_2 += net_salary
        income_tax_2= gross_salary - net_salary
        total_income_tax_2 += income_tax_2
        print("Net Salary: ", net_salary, ", Income Tax: ", income_tax_2)
    else:
        net_salary = gross_salary * 0.75
        number_of_high += 1
        total_net_salary_3 += net_salary
        income_tax_3 = gross_salary - net_salary
        total_income_tax_3 += income_tax_3
        if gross_salary > 50000:
            more_than_fifty += 1
        print("Net Salary: ", net_salary, ", Income Tax: ", income_tax_3)
    total_gross_salary += gross_salary
    gross_salary = int(input("Gross Salary: "))
average = (total_net_salary_3 + total_net_salary_2 + total_net_salary_1) / (number_of_low+number_of_medium+number_of_high)
incometax = total_income_tax_1 + total_income_tax_2 + total_income_tax_3
percentage_of_incometax = (total_income_tax_1 + total_income_tax_2 + total_income_tax_3)/total_gross_salary*100
prcntg_morethan50000 = more_than_fifty/number_of_high*100
print(f"Number of low-salary sales representatives: {number_of_low} \nNumber of medium-salary sales representatives: {number_of_medium} \nNumber of high-salary sales representatives: {number_of_high}")
print(f"Percentage of those with a gross salary of more than 50000 (among those with a gross salary of more than 25000): %{prcntg_morethan50000:.2f}")
print(f"Average net salary of all sales representatives: {average:.2f}")
print("Total income tax: ", incometax)
print(f"Percentage of total income tax in total gross salary: %{percentage_of_incometax:.2f}")





