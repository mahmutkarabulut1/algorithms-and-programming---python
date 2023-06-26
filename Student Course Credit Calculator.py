student_id = input("student id: ")
name_and_surname = input("name and surname: ")
weekly_theoretical_course_hours_of_the_first_course = int(input("weekly theoretical course hours of the first course: "))
weekly_practical_course_hours_of_the_first_course = int(input("weekly practical course hours of the first course: "))
ECTS_credits_of_the_first_course = int(input("ECTS credits of the first course: "))
term_grade_of_the_first_course = float(input("term grade of the first course: "))
weekly_theoretical_course_hours_of_the_second_course = int(input("weekly theoretical course hours of the second course: "))
weekly_practical_course_hours_of_the_second_course = int(input("weekly practical course hours of the second course: "))
ECTS_credits_of_the_second_course = int(input("ECTS credits of the second course: "))
term_grade_of_the_second_course = float(input("term grade of the first course: "))

total_amount_of_local_credits_taken_this_semester = weekly_theoretical_course_hours_of_the_first_course + weekly_theoretical_course_hours_of_the_second_course + weekly_practical_course_hours_of_the_first_course /2 + weekly_practical_course_hours_of_the_second_course/2
total_amount_of_ECTS_credits_taken_this_semester = ECTS_credits_of_the_first_course + ECTS_credits_of_the_second_course
print ("total amount of credits taken this semester =", total_amount_of_local_credits_taken_this_semester)
print ("total amount of ECTS credits taken this semester=", total_amount_of_ECTS_credits_taken_this_semester)

WGPA_based_on_local_credit_at_the_end_of_this_semester = (((weekly_theoretical_course_hours_of_the_first_course + weekly_practical_course_hours_of_the_first_course/2) * term_grade_of_the_first_course) + term_grade_of_the_second_course * (weekly_theoretical_course_hours_of_the_second_course + weekly_practical_course_hours_of_the_second_course/2)) / total_amount_of_local_credits_taken_this_semester
print ("WGPA based on local credit at the end of this semester=", WGPA_based_on_local_credit_at_the_end_of_this_semester)
WGPA_based_on_ECTS_at_the_end_of_this_semester = (ECTS_credits_of_the_first_course * term_grade_of_the_first_course + ECTS_credits_of_the_second_course * term_grade_of_the_second_course) / total_amount_of_ECTS_credits_taken_this_semester
print ("WGPA based on ECTS at the end of this semester=", WGPA_based_on_ECTS_at_the_end_of_this_semester)





