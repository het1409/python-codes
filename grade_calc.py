marks = int(input("Enter your marks: "))

#definig rules
'''
**`Letter Grade Ranges**:`

- `A: 90-100`
- `B: 80-89`
- `C: 70-79`
- `D: 60-69`
- `F: 0-59`
'''

if marks >= 90 and marks <= 100:
    print("Your grade is A")
elif marks >= 70 and marks <= 79:
    print("Your grade is B")
elif marks >=60 and marks <=69:
    print("Your grade is C")
else:
    print("Your grade is D")