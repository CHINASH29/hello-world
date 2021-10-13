students_num = int(
    input('Enter the no of students you want to take input for: '))

register = []
names = []
acheives = []

for detail in range(students_num):
    print()
    regno = int(input("Enter the student's register no: "))
    register.append(regno)
    stud_name = str(input("Enter student's name: "))
    names.append(stud_name)
    achievement = str(input("Enter the student's achievement: "))
    acheives.append(achievement)
    print('\nDETAILS OF {} STUDENT'.format(detail + 1))
    print('{} {} {}'.format(regno, stud_name, achievement))

print()
print("\n-------REGISTER NUMBERS-------")
for regs in register:
    print('Register No:- {}'.format(regs))

print()
print('------------DETAILS OF STUDENTS EXCEPT REGISTER NUMBER------------')
for n in names:
    print('NAME:- {}'.format(n))

print()
for a in acheives:
    print('ACHIEVEMENT:- {}'.format(a))
