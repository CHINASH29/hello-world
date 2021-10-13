print("WELCOME TO FINAL YEAR OF BCA 2020-2021")
A = []
n = int(input("Enter the number of students that you want ?"))
for i in range(n):
    name = input("Enter your name")
    regno = input("Enter your regestration number")
    division = input("Enter your Division")
    print("Enter your choice that you are interested in:")
    print("1.Attendence and CIA")
    print("2.Attendence Recorder")
    print("3.MIDSEM AND SCORES")
    print("4.TIME TABLE")
    print("5.TOP 10 SCORED")
    print("6.HOURS ATTENDED ON THAT DAY")
    Continue = 'C'
    while Continue == 'C' or Continue == 'c':
        choice = input("CHOOSE THE CHOICE FROM THE ABOVE")
        if choice in ('1', '2', '3', '4', '5', '6'):
            if choice == '1':
                conducted = 150
                present = int(input("Enter the number of days present"))
                absent = int(input("Enter the number of days absent"))
                totalatten = float(present/conducted)*100
                print("The number of days present:", present)
                print("The number of days absent:", absent)
                print("The number of classes conducted:", conducted)
                print("The total percnetage is:", totalatten)
                print("\n The TOTAL CIA MARKS ARE:")
                print("\nEnter the CIA I marks:-")
                test = float(input("Enter the Component 1 of CIAI"))
                test1 = float(input("Enter the Component 2 of CIAII"))
                total = test+test1
                CIA1 = float(total*0.5)
                print("The CIA I mark is:", CIA1)
                mid = int(input("\nENTER THE CIA 2/MIDSEM MARKS OUT OF 50:-"))
                CIA2 = mid*0.5
                print("The CIA II mark is:", CIA2)
                print("\nEnter the CIA III marks:-")
                test = float(input("Enter the Component 1 of CIAIII"))
                test1 = float(input("Enter the Component 2 of CIAIII"))
                total = test+test1
                CIA3 = float(total*0.5)
                print("The CIA III mark is:", CIA3)
                components = CIA1+CIA2+CIA3
                if(totalatten >= 95):
                    component = component+5
                    print("The total CIA with attendence is:", component)
                else:
                    print("Completed without attendence")
            elif choice == '2':
                conducted = 87
                python = int(
                    input("Enter the number of python hours atttended(out of 30)"))
                CN = int(
                    input("Enter the number of computer network hours attended(out of 10)"))
                GA = int(
                    input("Enter the number of Graphics and animation hours attended(out of 15)"))
                Multimedia = int(
                    input("Enter the number of Mutimedia hours attended(out of 20)"))
                project = int(
                    input("Enter the number of project hours attended(out of 12)"))
                present = python+CN+GA+Multimedia+project
                totalatten = float(present/conducted)*100
                print("\n The number of hours attended in python is:", python)
                print("\n The number of hours attended in CN is:", CN)
                print("\n The number of hours attended in GA is:", GA)
                print("\n The number of hours attended in Multimedia is:", Multimedia)
                print("\n The number of hours attended in project is:", project)
                print("\n The number of hours attended in total is:", present)
                print("\n The total percentage of attendence is:", totalatten)
                if(totalatten >= 85):
                    print("Student doesn't require to get claims:-")
                else:
                    print("Student have to get claims:-")

            elif choice == '3':
                attended = int(
                    input("Did the student attend the mid semester:-"))
                if(attended == 1):
                    python = int(input("Enter the python mark(out of 50):"))
                    CN = int(input("Enter the CN mark(out of 50):"))
                    GA = int(input("Enter the GA mark(out of 50):"))
                    MA = int(input("Enter the MA mark(out of 50):"))
                    total = python+CN+GA+MA
                    midsem = total*0.5
                    print("The midsem mark is:-", midsem)
                else:
                    print("Re-Exam is allowed with 10% detuction")
                    python = int(input("Enter the python mark(out of 50):"))
                    CN = int(input("Enter the CN mark(out of 50):"))
                    GA = int(input("Enter the GA mark(out of 50):"))
                    MA = int(input("Enter the MA mark(out of 50):"))
                    total = python+CN+GA+MA
                    midsem = total*0.5-(10/100)
                    print("The midsem mark is:-", midsem)

            elif choice == '4':
                print("\n\t******TIME TABLE*****\n")
                print("\t  DATE\t\t\tSUBJECT")
                print("\t 4.8.2020\t\tPython")
                print("\t 7.8.2020\t\tCN")
                print("\t 11.8.2020\t\tGA")
                print("\t 14.8.2020\t\tMutimedia")
                print("\n\t**********************\n")

            elif choice == '5':
                python = int(input("\nEnter the python mark(out of 50):"))
                CN = int(input("\nEnter the CN mark(out of 50):"))
                GA = int(input("\nEnter the GA mark(out of 50):"))
                MA = int(input("\nEnter the MA mark(out of 50):"))
                total = python+CN+GA+MA
                midsem = total*0.5
                print("\nThe midsem mark is:", midsem)
                A.append(midsem)
                for i in range(len(A)):
                    min_index = i
                    for j in range(i+1, len(A)):
                        if A[min_index] > A[j]:
                            min_index = j
                    A[i], A[min_index] = A[min_index], A[i]

                print("Sorted Array of marks is:-")
                for i in range(len(A)):
                    print("%d" % A[i])

            elif choice == '6':
                hour = 0
                hour1 = 0
                hour2 = 0
                hour3 = 0
                Python = int(input("Did the student attend Python class"))
                if(Python == 1):
                    hour = 1
                    print("Student is present")
                else:
                    print("Student is absent")

                CN = int(input("Did the student attend CN class"))
                if(CN == 1):
                    hour1 = 1
                    print("Student is present")
                else:
                    print("Student is absent")

                GA = int(
                    input("Did the student attend Graphics and animation class"))
                if(GA == 1):
                    hour2 = 1
                    print("Student is present")
                else:
                    print("Student is absent")

                MU = int(input("Did the student attend Multimedia class"))
                if(GA == 1):
                    hour3 = 1
                    print("Student is present")
                else:
                    print("Student is absent")

                print("The total number of hours present on that day is:")
                totalhours = hour+hour1+hour2+hour3
                print("\n The hours present is", totalhours)
        else:
            print("INVALID INPUT")
        Continue = input("Press C/c to Continue or Any Key to exit")
        print()
