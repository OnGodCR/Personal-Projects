#Name Script

name = input("What's your name? ").title().strip()
Fn, Ln = name.split(" ")
print("Hello, Mr. " ,Ln,".", sep="")
operation = input("What would you like to perform? (Addition, Subtraction, Multiplication, Division) ").title().strip()

#Operation Script

if operation == "Addition":
     n1 = input("What would be the first number you would like to add? ")
     n2 = input("What would be the second number you would like to add? ")
     answer = float(n1)+float(n2)
if operation == "Subtraction":
    n1 = input("What would be the number you would like to subtract from? ")
    n2 = input("What would be the number you are subtracting? ")
    answer = float(n1)-float(n2)
if operation == "Multiplication":
    n1 = input("What would be the number you would like to multiply? ")
    n2 = input("What would be the number you would like to multiply with? ")
    answer - float(n1)*float(n2)
if operation == "Division":
    n1 = input("What would be the number you would like to divide from? ")
    n2 = input("What would be the number you want to divide by? ")
    answer = float(n1)/float(n2)

#Print Answer Script

print("Mr. ", Ln, "your answer is", answer)