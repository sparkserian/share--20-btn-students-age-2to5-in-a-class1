# share-$20-btn-students-age-2to5-in-a-class1
 
#write a program to share $20 among students who are between the ages of 2 and 5 years in a class.

def main():
    money = 20
    students = int(input("Enter number of students between 2 and 5: "))
    print("Each student should receive ${:.2f}".format(money/students))
main()
