

import xml.etree.ElementTree as ET
myTree = ET.parse('student.xml')
myroot = myTree.getroot()
print(myroot.tag)


for x in myroot.findall('Student'):
    id = x.find('id').text
    name = x.find('name').text
    course = x.find('program').text
    grade = x.find('grade').text

    print('\n--------------------------------------------------------\n')
    print('ID       : {}\n'.format(id))
    print('NAME     : {}\n'.format(name))
    print('COURSE   : {}\n'.format(course))
    print('GRADE    : {}\n'.format(grade))


ide = input('ID :')
name = input('Name :')
course1 = input('Course :')
grade1 = input('Grade  :')


child = ET.Element("Student")
myroot.append(child)


id = ET.SubElement(child, 'id')
id.text = ide
nm = ET.SubElement(child, "name")
nm.text = name
program = ET.SubElement(child, "program")
program.text = course1
grade = ET.SubElement(child, "grade")
grade.text = grade1


myTree.write('student.xml')


ide = input('ID :')
name = input('Name :')
salary = input('Course :')
designation = input('Grade  :')


child = ET.Element("Employee")
myroot.append(child)


id = ET.SubElement(child, 'ID')
id.text = ide
nm = ET.SubElement(child, "name")
nm.text = name
program = ET.SubElement(child, "Salary")
program.text = salary
grade = ET.SubElement(child, "Designation")
grade.text = designation


myTree.write('student.xml')
