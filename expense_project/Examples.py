##List
nums = [1,2,3,4,5,6]                

for n in nums:
    if  n % 2 == 0:
        print("Even:", n)
    else:
        print("Odd:", n)



## Dictionary
 
student ={                      
    "name": "Aman",
    "age": 25
    }

print(student["name"])

## Function

def add(a,b):
    return a+b

print(add(2,5))
## OOP
class student:
    def __init__(self,name):
        self.name = name

s1 = student("Aman")

print(s1.name)

## File handling
##
##with open("test.txt", "w") as file:
##           file.write("Hello")
##
##with open("test.txt", "r") as file:
##          print(file.read())
##
####Exception
try:
    n = int(input("Enter number"))
    pritn(n)

except:
    print("Invalid input")

##set prog
nums = [1,2,1,2,3]
print(set(nums))

##tupel
t = (1,2,3,4,5)
print(t)
##pandas
##import pandas as pd
##
##df = pd.read_csv("data.csv")
##
##print(df)

##loop

for i in range(1,11):
    print(i)

##prime number
n = 7

for i in range(2,n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

##String Reverse

text = "Pyhton"

print(text[::-1])

