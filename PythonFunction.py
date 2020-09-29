#Functions Python
def addition(num1,num2):
    answer = num1 + num2
    return answer
first_number = int(input("Please enter 1st number:\n"))
second_number = int(input("Please enter 2nd number:\n"))
result = addition(first_number,second_number)
print(result)
print(addition(7,6)*2) #reuse the function

#factorial
number = 7
factorial = 1
while number > 1:
    factorial=factorial * number
    number-= 1
print(factorial)

def fact(num):#Function and parameter
    #if statement
    if num < 2:
        return 1
    else:
        sum = num * fact(num -1)
        return sum
put_num =int(input("Please enter a number:"))#input() a public input
result=fact(put_num)
print(result)

#Recursion
def recursion(n):
    if n == 1:
        return  1
    return  n + recursion(n-1)
print(recursion())