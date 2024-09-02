#(8).Find Out pass-percentage of a class.
#A teacher is entering the marks students.
#A student passes a course if the marks are at least 40 (out of 100). The teacher wants to know the percantage of student passed.

n= int(input("Enter Number Of Student :"))
i=1                                          #initialion
pass_count= 0                  #pass is a reserved keyword in python so we took pass_count

while i<=n:                                   #condition
    marks=int(input("Enter Student Marks :"))

    if marks >=40:
        pass_count=+1
    i=i+1
print(pass_count*100/n,"% Student Passed ")
