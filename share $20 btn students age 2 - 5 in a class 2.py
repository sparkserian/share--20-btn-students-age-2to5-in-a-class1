#write a program to share $20 among students who are between the ages of 2 and 5 years in a class.

def main():
    print("This program will share $20 among students who are between the ages of 2 and 5 years in a class.")
    print("Please enter the number of students in the class:")
    num = int(input())
    print("Please enter the age of each student:")
    age = []
    for i in range(num):
        age.append(int(input()))
    total = 0
    for i in range(num):
        if age[i] >= 2 and age[i] <= 5:
            total += 1
    print("The number of students between 2 and 5 years old is:", total)
    print("The total amount to be received by each student is: ${:.2f}".format(20/total))
main()