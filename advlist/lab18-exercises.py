import random

wordbank= ["indentation", "spaces"] 
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
#added the number 4 to the list wordbank
wordbank.append(4)
print(wordbank)

choice = input("Please input a number between 0 and 18 or a students' name")

if choice not in tlgstudents:
    student_name = tlgstudents[int(choice)]
else:
    student_name = choice

print(f"{student_name} always uses {wordbank[-1]} {wordbank[-2]} to indent")


