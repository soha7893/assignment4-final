#Q 4 Calculate Average Marks
input_user_mark = int(input("How many marks do you want to enter?  "))
total_marks = 0
count = 1
while count <= input_user_mark:
    mark = float(input(f"Enter mark {count} "))
    total_marks += mark
    count +=1
average = total_marks / input_user_mark
print (f"Average: {average}")
print ( 50* "=" )
#Another solution using for loop
total_marks = 0
input_user_mark = int(input("How many marks do you want to enter?  "))
for i in range(1, input_user_mark+1):
    mark = float(input(f"Enter mark numbe {i}  "))
    total_marks += mark
average = total_marks / input_user_mark
print(f"Average: {average}")   