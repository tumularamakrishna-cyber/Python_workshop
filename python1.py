roll_numbers = [1, 2, 9, 3, 5, 7, 11, 13, 12, 10, 14, 15, 16, 18]
new_roll = int(input("Enter roll number: "))
found = False
for r in roll_numbers:
    if r == new_roll:
        found = True
        break
if found:
    print("Roll number already exists")
else:
    roll_numbers.append(new_roll)
    print("Roll number inserted")
print("Updated list:", roll_numbers)