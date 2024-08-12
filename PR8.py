Stdnt_Count=int(input("Total no of student : "))
c=0
passed=0
if Stdnt_Count>0:
    for i in range(1,Stdnt_Count+1):
        marks=int(input("Enter student "+str(i)+" marks : "))
        if marks>=40:
            passed+=1
    per=(passed*100)/Stdnt_Count
    print(per,"% Students Passed...")
else:
    print("Please Enter correct students numbers. ")