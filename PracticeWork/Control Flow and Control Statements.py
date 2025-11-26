#1. Check if three lengths form an Equilateral, Isosceles, or Scalene triangle
a, b, c = tuple(map(int, input().split()))

if a == b and a==c and b == c:
                print("Equ")
elif a != b and b != c and a != c:
    print("Sca")
else:
    print("Iso")

#2. Classify a character as: vowel, consonant, digit, special character
ch = input()

vol = 'aeiouAEIOU'

if ch in vol:
    print("Vol")
elif ch.isalpha():
    print("Con")
elif ch.isdigit():
    print("Dig")
else:
    print("Special")

#3. BMI Calculator and Category

height = float(input())
weight = float(input())
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
print(bmi)

#4. Electricity bill calculator based on units used

units = int(input())
charge = 0

if units <= 100:
    charge = units * 1
elif 100 < units <= 200:
    charge = 100 + (units - 100) * 2
else:
    charge = 300 + (units - 200) * 3

print(charge)

#5. Check if a number is Armstrong

num = input()
res = 0
l = len(num)

for i in num:
    res += int(i) ** l

if res == int(num):
    print("Arm")
else:
    print("Not Arm")
    
print(res)

#6. Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 specialchar)

password = input("Enter password: ")

if len(password) >= 8:
    if any(ch.isupper() for ch in password):
        if any(ch.isdigit() for ch in password):
            if any(ch in "!@#$%^&*()-_=+[]{};:'\",.<>?/|" for ch in password):
                print("Strong Password")
            else:
                print("Weak Password")
        else:
            print("Weak Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")

#7. ATM Withdrawal Simulation

balance = int(input())
withdrawal = int(input())
if withdrawal >= 500 and withdrawal % 100 == 0 and withdrawal <= balance:
    balance -= withdrawal
    print("Success")
    print(balance)
else:
    print("Insufficient Balance")

#8. Ticket fare calculator with age-based discounts

age = int(input())
price = 200
fare = 0

if age < 5:
    fare = 0
elif 5 <= age <= 18:
    fare = 100 - 100 * 0.5
elif age > 60:
    fare = price - price * 0.3
else:
    fare = price

print(fare)

#9. 24-hour to 12-hour time converter
'''
Question: Convert format with AM/PM using conditional logic.
Test Cases:
Input: 13:45 → Output: 1:45 PM
Input: 00:15 → Output: 12:15 AM
'''
time = input()
hours, minutes = map(int, time.split(":"))
period = "AM"
if hours == 0:
    hours = 12
elif hours == 12:
    period = "PM"
elif hours > 12:
    hours -= 12
    period = "PM"
print(f"{hours}:{minutes:02d} {period}")

