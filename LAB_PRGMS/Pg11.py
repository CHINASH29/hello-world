import xml.etree.ElementTree as ET

tree = ET.parse('student.xml')
root = tree.getroot()

print("\n\n\t\tXML FILE HANDLING")
print("\t\t-----------------\n\n")


print('Student Details')
print('---------------\n')

for elem in root:
    for subelem in elem:
        print(subelem.attrib, " : ", subelem.text)
    print('\n')

id = ""
name = ""
program = ""
grade = ""
dept = ""


def check_id():
    x = False
    while(x == False):
        id = input('Enter ID : ')
        if(id.isdigit() == True and len(id) == 7):
            return id
        else:
            print('Invalid ID')


def check_name():
    x = False
    while(x == False):
        name = input('Enter Name : ')
        if(name.isalpha()):
            return name
        else:
            print('Invalid Name')


def check_program():
    x = False
    p = ['BCA', 'BBA', 'MCA', 'MBA', 'BCom']
    while(x == False):
        program = input('Enter Program : ')
        if(program in p):
            return program
        else:
            print('Invalid Program')


def check_grade():
    x = False
    p = ['A', 'B', 'C', 'D']
    while(x == False):
        grade = input('Enter Grade : ')
        if(grade in p):
            return grade
        else:
            print('Invalid Grade')


def check_dept():
    x = False
    p = ['Computer', 'Mathematics', 'Physics',
         'Chemistry', 'Arts', 'Commerce', 'Humanities']
    while(x == False):
        dept = input('Enter Department : ')
        if(dept in p):
            return dept
        else:
            print('Invalid Department')


answer = 'y'

while(answer == 'y'):
    print('\n\nCHOOSE FROM MENU')
    print('1. Add a student')
    print('2. Modify student details')
    print('3. Add an employee')
    print('4. Modify employee details')
    print('5. Show Details\n')
    choice = input('Choice : ')

    if(choice == '1'):
        id = check_id()
        print('\n')
        name = check_name()
        print('\n')
        program = check_program()
        print('\n')
        grade = check_grade()

        child = ET.SubElement(root, 'child')
        i1 = ET.SubElement(child, 'ID')
        i2 = ET.SubElement(child, 'sname')
        i3 = ET.SubElement(child, 'program')
        i4 = ET.SubElement(child, 'grade')

        i1.set('name', 'ID')
        i1.text = id
        i2.set('name', 'Name')
        i2.text = name
        i3.set('name', 'Program')
        i3.text = program
        i4.set('name', 'Grade')
        i4.text = grade

        mydata = ET.tostring(root)
        with open("student.xml", "wb") as f:
            f.write(mydata)

        print('Student added successfully')

    elif(choice == '2'):
        n = input('\nEnter the student name whose details has to be modified : ')
        i = 0
        for child in root.findall('child'):
            na = child.find('sname').text
            if(n == na):
                i = 1
                print('\nChoose the detail to be modified')
                print('1. ID')
                print('2. Name')
                print('3. Program')
                print('4. Grade')
                c = input('Choice : ')

                if(c == '1'):
                    id = check_id()
                    b = child.find('ID')
                    b.text = id
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('ID modified successfully')

                elif(c == '2'):
                    name = check_name()
                    b = child.find('sname')
                    b.text = name
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('Name modified successfully')

                elif(c == '3'):
                    program = check_program()
                    b = child.find('program')
                    b.text = program
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('Program modified successfully')

                elif(c == '4'):
                    grade = check_grade()
                    b = child.find('grade')
                    b.text = grade
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('Grade modified successfully')

                else:
                    print('Invalid choice')
                break

        if(i == 0):
            print('Student not found')

    elif(choice == '3'):
        id = check_id()
        name = check_name()
        dept = check_dept()

        child = ET.SubElement(root, 'employee')
        i1 = ET.SubElement(child, 'ID')
        i2 = ET.SubElement(child, 'ename')
        i3 = ET.SubElement(child, 'dept')

        i1.set('name', 'ID')
        i1.text = id
        i2.set('name', 'Name')
        i2.text = name
        i3.set('name', 'Department')
        i3.text = dept

        mydata = ET.tostring(root)
        with open("student.xml", "wb") as f:
            f.write(mydata)

        print('\nEmployee added successfully')

    elif(choice == '4'):
        n = input('\nEnter the employee name whose details has to be modified : ')
        i = 0
        for child in root.findall('employee'):
            na = child.find('ename').text
            if(n == na):
                i = 1
                print('\nChoose the detail to be modified')
                print('1. ID')
                print('2. Name')
                print('3. Department')
                c = input('Choice : ')

                if(c == '1'):
                    id = check_id()
                    b = child.find('ID')
                    b.text = id
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('ID modified successfully')

                elif(c == '2'):
                    name = check_name()
                    b = child.find('ename')
                    b.text = name
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('Name modified successfully')

                elif(c == '3'):
                    dept = check_dept()
                    b = child.find('dept')
                    b.text = dept
                    mydata = ET.tostring(root)
                    with open("student.xml", "wb") as f:
                        f.write(mydata)
                    print('Department modified successfully')

                else:
                    print('Invalid choice')
                break

        if(i == 0):
            print('Employee not found')

    elif(choice == '5'):
        for elem in root:
            for subelem in elem:
                print(subelem.attrib, " : ", subelem.text)
            print('\n')

    else:
        print('Invalid Choice')

    answer = input('\n\nDo you want to try other options (y/n) : ')
