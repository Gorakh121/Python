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

