"""
#no function

num = int(input("How many exam grades  dose each student have? "))
while True:
    total = 0
    print('Enter the exam grades')
    for i in range(1, num + 1):
        grade = float(input("Exam " + str(i) + ": "))
        total += grade
    avg = total / num
    print("The average is:", round(avg, 2))
    rep = input("Enter exam grades for another student? (y/n): ")
    if rep != 'y':
        break
"""
#w.fun
def avg():
    n = int(input("How many exam grades does each student have? "))
    s = 0
    print("Enter the exam grades.")
    
    for i in range(1, n + 1):
        grade = float(input("Exam " + str(i) + ": "))
        s = s + grade
    
    print("The average is", s / n)


while True:
    avg()
    
    again = input("Enter exam grades for another student (Y/N)? ")
    if again == "n":
        break
