clicks = [10, 5, 15, 20]
doubled_list = list()
for c in clicks:
    doubled_list.append(c*2)
print(doubled_list)
    

student_score = [70, 60, 55, 64, 83, 22]
passed_student = [s for s in student_score if s >= 60]
print(passed_student)


prodect = ['apple', 'banana', 'orange', 'orange']
cleaned_prodect = [p for p in prodect if prodect.count(p) == 1]
print(cleaned_prodect)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [n for row in matrix for n in row]
print(flattened_matrix)


ages = [22, 34, 25, 11, 15, 33, 65]
print(sum(age for age in ages if age > 20))
print([age for age in ages if age >= 20])


list =['cofee', 'tea', 'latte', 'coffee', 'tea', 'latte', 'coffee', 'tea', 'latte']
price = [(item, 3.5) for item in list]
print(price)


scores = [70, 60, 50, 55, 62, 58, 75, 85]
passed_doubled = [s * 2 for s in scores if s >= 50]
print(passed_doubled)


my_friends = ['ahmed jamac ', 'ahmed maxamed', 'nasrudiin halane']
s1 = [item.capitalize() for item in my_friends]
print(s1)

reversed_name = [item[::-1] for item in my_friends]
print(reversed_name)

math = [8, 18, 24, 16, 21, 25, 64]
devisible_by_eight = [m for m in math if m % 8 == 0]
print(devisible_by_eight)

math_str = [str(m) for m in math]
print(math_str)
print('-'.join(math_str))
print([item[::-1] for item in math_str])

password = [str(p) for p in range(10)]
print(''.join(password))

