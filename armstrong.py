# armstrong number is a number with sum of its digit's cube
# 153 -> 1^3+5^3+3^3 = 153
# 370,371,470

number = int(input("enter a number to check for armstrong : "))
temp = number
armstrong_sum = 0
while number > 0:
    digit = number % 10
    armstrong_sum = armstrong_sum + digit ** 3
    number = number // 10 # // floor division operator
if temp == armstrong_sum:
    print(temp, "is an armstrong number")
else:
    print(temp, "is not an armstrong number")
