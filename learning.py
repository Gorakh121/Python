# print("hello world\n") #comment
# print("hey")
# print("prayas baral", "priya sharma")
# print(45)
# print(43+23)
# name = "prayas" #string
# age = 56
# price = 56000.89
# t = False
# y = None
# print(name ,age, price)
# print("Name is", name ,"Age is:", age ,"price is:", price)

# print(type(name))  #to detect the  data type 
# print(type(age))
# print(type(t))
# print(type(y))


# #for boolean function we must write capital letter of startinf of true and fasle

# a = 5
# b = 6
# c = a+b
# print(c)

# print(a**b) #a ko power b

# #type conversion
# g = int("2") #converted into integer
# a = 5
# b =  4.3
# sum = a+b #converted into float by itseld
# print(sum)
# print(type(g))

# Taking input
# name = input("Enter the name of the person:")
# print("he is the one",name)

# val = int(input("Enter the value"))
# print(val)

#string

# str = "This is a string.\n We are a boy" #use of escape sequence
# print(str) 

#concatenation

# str1 = "Prayas"
# str2 = "Baral"
# print(str1+str2)


#length

# str1 = "Prayas"
# str2 = "Baral"
# final = str1 + " " + str2
# print(final)
# print(len(final))

#indexing
# str = "Prayas"
# ch = str[3]
# print(ch) 


#slicing (accessing parts of a string)
# str = "Prayas"
# ch = str[1:5]
# print(ch)

#negative indexing starts with -1 and soon and -1 is the last string
# str = "Prayas"
# print(str[-4:-1])


#string function
# str = "prayas is  a sojo boy"
# print(str.endswith("oey"))  #checks whether the string ends with the given string or not
# a = str.capitalize()  #capitalize the first string
# print(a)

# b = str.replace("o", "a") #replace the words from the given string
# print(b)

# c = str.find("sojo")  #find the index of the given strings
# print(c)

#count the strings
# d = str.count("o") 
# print(d)


#wap to input user & print its length
# a = input("Enter the strings\n")
# print(len(a))


# #wap to find the occurence of "S" in the string
# b = input("Enter the string value\n")
# print(b.count("S")) 


#condition statements
# 1
# age = 32
# if (age >= 18):
#     print("Can vote")
# else:
#     print("can't vote")
    
    #2
# light = "red"
# if (light == "red"):
#         print("stop")
# elif(light== "green"):  #indentation means proper spacing (curly bracket is not used so)
#         print("go")
# elif(light== "yellow"):
#         print("look")


#3
# num = int(input("Enter the student's marks:\n"))

# if(num>=90):
#     grade = "A"
# elif(num>=80 and num<=90):
#     grade = "B"
# elif(num>=70 and num>=80 ):
#     grade = "C"
# else:
#     grade = "D"
    
#     print("Student got :", grade)

#nesting 
# age = int(input("Enter the age:\n"))
# if(age>=18):
#     if(age>=80):
#         print("cant")
#     else:
#         print("can")
# else:
#     print("cant")

#wap to check if a number entered by the user is odd or even
# num = int(input("Enter the number:\n"))
# if(num%2 == 0):
#     p = "even"
# else:
#     p = "odd"
    
# print("The number you entered is:", p)


#wap to find the greatest of 3 numbers entered by the user
# a = int(input("Enter the 1st number:"))
# b = int(input("Enter the 2nd number:"))
# c = int(input("Enter the 3rd number:"))
# if(a>b and a>c):
#    print("The greatest number is first number", a)
# elif(b>a and b>c):
#     print("The greatest number is second number", b)
# elif(c>a and c>b):
#    print("The greatest number is third number", c)

    





#wap to check if a number is multiple of 7 or not
# a = int(input("Enter the number:\n"))
# if(a%7==0):
#     b= "multiple of 7"
# else:
#     b = "not a multiple of 7"
    
# print(b)


#list and tuple => array
# age =  [12,34,54,54,34,32]
# print(age)
# print(type(age))
# print(age[3])
# print(len(age))

# student  = ["karan", 43,"delhi"]
# student[0]= "Prayas"  #updated
# print(student)
# print(len(student)) # finding the of length list 
# print(student[1:2])  #slicing


#list methods
# list = [2,56,43,65,2,123]
# a = ["Prayas", 67,"baral"]
# list.append(5) #add the value to the last index of the list
# list.sort() #assending order
# list.sort(reverse=True) #descending order it also works in the string
# list.reverse()#reversse the list but not letter by letter it only works for word by word
# a.reverse()
# print(a)
# list.insert(0,56) #insert the value in the list in the given index
# list.pop(2) #deleted the value of the given index
# print(list)


# #tuples
# tup = (2,4,5,6,7)
# print(tup.index(2))   #provides the  index of the given value
# print(tup.count(2)) #count the no. of value repeated


#questions

#wap to ask the user to enter names fo their 3 fav movies & store them in a list
# mov = []
# mov.append(input("Enter your 1st fav movies:\n"))
# mov.append(input("Enter your 1st fav movies:\n"))
# mov.append(input("Enter your 1st fav movies:\n"))

# print(mov)

#wap to check if a list contains a palindrome of elements 

# list = []
# list.append(int(input("Enter the list1 value:\n")))
# list.append(int(input("Enter the list1 value:\n")))
# list.append(int(input("Enter the list1 value:\n")))
# print(list)
# copy = list.copy()
# copy.reverse()

# if (copy == list):
#     print("Palindrome")
# else:
#     print("Not a palindrome")



#dictionay 
# info = {
#     "key" : "value",
#     "name" : "Prayas"
# }

# info["key"] = "prayas"  #modify the value
# print(info)

#dictionary methods

# student ={
#     "name":"Prayas",
#     "age":45
# }
# print(student.keys()) #print all the keys
# print(list(student.keys())) #print all the keys in the list form
# print(len(list(student.keys()))) #print the no of keys in the list

# print(student.values()) #return the values
# print(list(student.values()))

# print(student.items()) #return it into tuple

# # print(student.get("age")) #return specified values
# student.update({"city":"ktm"}) #add values & keys
# print(student)


#set
# set = {1,2,3,4,5} #if the values is repeated then python ignores that values
# set1 = {2,3,5,6,8,10}
# settt = set() #it is the empty set
# set.add(34)
# set.remove(3)
# set.clear()
# set.pop() #delete any values
# set3 = set.union(set1)  
# set4 = set.intersection(set1)
# print(set4)
# print(set3)
# print(len(set3))

#store following word meanings in a python dictionary
# table = "a piece of furniture", list of facts and figures, cat: "a small animal"

# table = {
#     "table":["a piece of furniture",
#     "list of facts and figures"],
#     "cat":"a small animal"
# }
# print(table)

# you are given a list of a subjects for students. Assume one classroom is required for 1 subjects. How many clssrooms are needed by all ths students
#python, java, c++ python javascript java python jjava c++ c

# set = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }
# print(len(set))


#wap to enter marks of 3 subjects from the user and stokre themn in a dictionary. Start with an empty dictioinary and add one by one. Use subject names as key and marksk as value.

# student ={}
# student.update({input("Enter the key") : input("enter the value")})
# student.update({input("Enter the key") : input("enter the value")})
# student.update({input("Enter the key") : input("enter the value")})
# print(student)

#loop

# count = 1
# while count<=100:
#     print("hello",count)
#     count = count+1
    
#print the multiplication table of a number n
# a = int(input("Enter the no. to be multiplied:"))
# n = 1
# while n<=10:
#     print(a,"*",n,"=" ,a*n)
#     n +=1

#print the elements of the following list
#[1,4,9,16,25,36,49,64,81,100]

# a = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx< len(a):
#     print(a[idx])
#     idx +=1
    
#search for a number  x in the tuple using loop
# [1,4,9,16,25,36,49,64,81,100]

# a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter the value: "))
# i = 0

# while i < len(a):
#     if a[i] == x:
#         print("Found at index", i)
#         break
#     i += 1
# else:
#     print("Not found")

 #printing odd number 
 
# i = 1
# while i<=10:
#     if(i%2==0):
#         i += 1
#         continue
#     print(i)
#     i += 1

#use of for loop 
# list = [1,2,3,4,5,6,7]

# for num in list:
#     print(num)

#for tupple
# a = (4,5,6,7,7)
# for num in a:
#     print(num)

#for loop with else
# str = "Prayas"
# for a in str:
#     if (a == "y"):
#         print("found",a)
#         break
#     print(a)
# else:
#     print("END")

#1
#print the elements of the following list using Loop
# a= [1,4,9,45,45,45,45,34,23,67,67]
# for b in a:
#     print(b) 
 
 
 #2
 #search for a number x in this tuple using loop
# a = (45,45,34,23,2,56,7,87,89,565,34,23,1)
# x = int(input("Enter the number which you want to search:"))
# index = 0
# for b in a:
#     if (x ==b):
#         print("searched", index)
#         break
#     index +=1
# else:
#     print("not found")
   
   
#use of range()

# for a in range(10):  #range(stop)
#     print(a)

# for i in range(2,10): #range (starting and stoping vallue)
#     print(i)

# for i in range(2,20,2): # start end and increment value
#     print(i)
    
#1
#print numbers 1 to 100
# for i in range(1,101):
#     print(i)

#2
# #print number from 100 to 1
# for i in range(100,0,-1):
#     print(i)
 
 
 #multiplication of n
 
# a = int(input("Enter the number which you want to multiply:"))
# b = range(1,11)
# for b in b:
#     print(a,"*",b,"=", a*b)    

#pass statement
# for i in range(10):
#     pass  #use for future it is empty 

#1
#wap to find the sum of first n numbers (using while)
# i = 0
# sum= 0
# while(i<=9):
#     sum = sum +i
#     i +=1
#     print(sum)


#2
#wap to find the factorial of first numbers (using for)
# n= 5
# fact = 1
# i = 1
# for i in range(1,n+1):
#     fact = fact*i
    
# print(fact)


#qr code
# import qrcode
# qr_img = qrcode.make("https://www.facebook.com/prayasbaral2765")
 
# qr_img.save("qr.jpg")

#function

# def cal(a,b):
#     sum = a+b
#     print(sum)
#     return sum

# cal(3,4)

#types of function
#1 built in function   already defined in python
#2 user defined functions

#1
#waf to print the length of a list

# b = [2,34,56,"ktm", "prayas"]

# def a(e):
#     print(len(e))

# a(b)

#waf to print the elements of a list in a single line

# items = [3,5,6,7,7,"Prayas"]

# def y(a):
#     for b in a:
#         print(b, end=" ")  #print the value in the single line
        
# y(items)


#waf to find the factorial

# def a(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
    
#     print(fact)
#     return fact

# a(9)


# def convert (usd):
#     nep = usd*130
#     print(usd, "usd =", nep, "npr")


# convert(5)


#recursion call itself  repeatedly

# def show(n):
#     if n==0:   #base  case
#         return
#     print(n)
#     show(n-1)
    
# show(5)


# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(8))


#write a recursive function to calculate the sum of first n natural numbers

# def sum(n):
#     if(n==0):
#         return 0
 
#     return sum(n-1) +n
    
# print(sum(5))

# def sum(n):
#     if ( n==0):
#         return 0
    
#     return sum(n-1) +n

# print(sum(6))

#write a recursive function to print all elements in list
na= [2,45,3,2,5,6,"prayas", "Ram"]
def print_el(list,idx=0):
    if idx == len(list):
        return 0    
    print(list[idx])
    print_el(list,idx+1)
    
print_el(na)