#(5).Write a program to find out if the two blood groups match.

# # Total Blood Group
# # A+,B+,O+,AB+,A-,B-,O-,AB-

p1=input("Student1 Blood Group:")
p2=input("Student2 Blood Group:")
Student1=p1.upper()
Student2=p2.upper()

if Student1 and Student2=="A+" or Student1 and Student2=="B+" or Student1 and Student2=="O+" or Student1 and Student2=="AB+" or Student1 and Student2=="A-" or Student1 and Student2=="B-" or Student1 and Student2=="O-" or Student1 and Student2=="AB-":
    
    if(Student1==Student2):
        print("Student1 and Student2 Same Blood Group")
    else:
        print("Student1 and Student2 Different Blood Group")
else:
    print("Wrong Blood Group")


