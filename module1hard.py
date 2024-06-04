
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
count_0 = sum(grades[0])
avg_0 = sum(grades[0])/len(grades[0])
count_1 = sum(grades[1])
avg_1 = sum(grades[1])/len(grades[1])
count_2 = sum(grades[2])
avg_2 = sum(grades[2])/len(grades[2])
count_3 = sum(grades[3])
avg_3 = sum(grades[3])/len(grades[3])
count_4 = sum(grades[4])
avg_4 = sum(grades[4])/len(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students= sorted(students)
my_dict = {students[0]:avg_0,
           students[1]:avg_1,
           students[2]:avg_2,
           students[3]:avg_3,
           students[4]:avg_4}
print(my_dict)



