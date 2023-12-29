# # section 2
# #global keyword

# x=0 
# # def sum():
# #     return x  #if we won't modify x it will be returned normaly 
# # print(sum())

# # def sum ():
# #     x=x+1    # we modified x so function can't see x 
# #     return x
# # print(sum())

# #solve problem  by global keyword + var name

# def sum ():
#     global x
#     x=x+1
#     return x 
# print(sum())    

# def f1():
#     global x
#     x = x + 1  
#     return x
# def f2():
#     return x+1   # لو x=x+1ايرور
# def f3():
#     x = 5  
#     return x+1

# x = 0  
# print(f1())
# print(f2())
# print(f3()) 

#default arguments of function 

# def sum(a , c=4,b=3):
#     return a++c+b

# print(sum(3,b=5))

# copy in lists 
# 1 shallow copy : two var haver same refrence of single list
# a = [ 1 ,3  , 6 ,8 ,9 ,1 ,5]
# b=a

# 2 deep copy another var takes acopy of list then ever var has his own list
# b = list(a)
# #or 
# b= a[:]


# tup=([1,2],[1,2,3])
# tup[0][1]=1
# print(tup)
# # tuple not changable 

# z = ([1,3],[2,6])
# z [0][1] = 5 # here we change the list in tuple not the tuple
# print (z)

# t =  1 , 2 , 3 # packging nnnnnn
# x , y , z = t # unpackging

## dictiony ( have all porpotise that in list but have advantage (key,value))
# a = {}
# a[1] = "ahmed"
# a[2] = "mohamed"
# print (5 in a ) # this search key in dictionry

# for key , value in a.items() :
#     print (key , value ) # to iterate on the dictionary 
    
    
# sets and set comprehension
## sets 
# a = "afewfredfvbaadfv"
# z = {x for x in a if x not in "abc"} # give all elemnts that not in a 
# print (z) # out : {'w', 'f', 'd', 'e', 'v', 'r'}  


# List comprehension
# ints = [1, 3, 10]
# # [i * 2 for i in ints]  # [2, 6, 20]

# x=[[i, j] for i in ints for j in ints if i != j]
# print(x) #[[1, 3], [1, 10], [3, 1], [3, 10], [10, 1], [10, 3]]


#sec.4
#oop \
# class FirstClass: # Define a class object
#      def setdata(self, value): # Define class methods
#          self.data = value # self is the instance
#      def display(self):
#          print(self.data) 
         
         
         
# x = FirstClass() # Make two instances
# y = FirstClass() # Each is a new namespace


# print(x)
# print(y)
# print(isinstance(x, FirstClass))

# print("##########################")

# x.setdata("Ahmed") # Runs: FirstClass.setdata(y, Ahmed)
# y.setdata(3.14159) # Runs: FirstClass.setdata(y, 3.14159)
# x.display()
# y.display()

# print("##########################")

# x.data = "New value" # Can get/set attributes
# x.display()

# print("##########################")

# x.anothername = "spam" # Can set new attributes here too!
# print(x.anothername)



  ###Constructors with default values  
    
# class First:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance
#         # print("__init__ function is ready")
#     # def __del__(self):
#     #     print("destructor is ready")
#     def __add__(self,other):
#         return First("test obj",self.balance+other)  #"test obj"  name of object
    

# object1=First("amr")
# print(object1.name)
# print(object1.balance)
# #del object1
# #object1=First("ahmed000")
# #print(object1.name)
# c2=object1+230   #230 stored in other of add func. 
# print(c2.balance)


 ###inheritance
 
 
# class person:
#     def __init__(self,name,id_number):
#         self.name=name
#         self.id_number=id_number
#     def display(self):
#         print(self.name)
    
# class employee(person):
#     def __init__(self, name, id_number,salary,post):
#         self.salary = salary
#         self.post=post
#         super().__init__(name, id_number)
#         #person.__init__(self,name, id_number)

# a = employee("amr",34678890,2022006,"Dog")
# a.display()




# #class magic method (len)


# class Skills:

#     def __init__(self, skill):  # construct skill names

#         self. skill= skill

#     def __len__( self):          # det length of the skill

#         return len(self .skill)
    
#     def get_len( self):   

#         """

#         function returns your length of skill name

#         """
        
#         return len (self. skill)
    
#     def __str__ (self):         # setting new offset of Skills class
    
#         return "this is Skill class"


# new_skill= Skills("css")        # create new object

# print(f"{new_skill.skill} \n {len(new_skill)}\n {new_skill.get_len()}")
# print(new_skill.__str__())




# multiple inheritance 

# class parent:
#     def __init__(self,name) :
#         self.name=name

#     def display_name(self):
#         return f"your name is {self. name}"
    
# class child1 (parent):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age

# class child2 (child1,parent):

#     def __init__(self,age, name,heigh):
#         super().__init__(name,age)
#         self.heigh = heigh

#     def display_info1(self):
#         return f"name is {self.name} ang age {self .age} anf heigh {self.heigh}"
    
# obj1 = child1("amr", 18)
# print(obj1.display_name())

# obj2 = child2("omar",185,199)
# print(obj2.display_name())
# print(obj2.display_info1())




# class attribute an class instance 

# class parent :

#     name= "amr" # class attribute

#     def __init__(self,name2) :

#         self.name2=name2  # instance
# class child(parent):
#     def __init__(self, name2):
#         super().__init__(name2)

#     def display(self):
#         print(parent.name)


# obj1=parent("ahmed")
# #print(obj1.name)  # calling class name attribute 
# obj1.name="omar"
# print(obj1.name)

# #print(obj1.name2) # calling class instance attribute 

# obj2= child("ali")
# #print(obj2.name2)
# #obj2.display()



### function overloading

# def add(datatype,*args):    #FIRST WAY

#     if datatype =="int":
#         answer =0
    
#     if datatype == "str":
#         answer=""

#     for x in args :
#         answer =answer+x

#     print(answer)

# add("int",1,2,3,4,5)
# add("str","a","m","r")

#-----------------------------------------------------------


# def add (a=None , b=None):    #SECOND WAY

#     if a!=None and b ==None:
#         print(a)
#     else:
#         print(a+b)
# add(2,3)
# add(22) 

#-----------------------------------------------------------

#from multipledispatch import dispatch

# @dispatch(int,int)
# def add(a,b):
#     print(a+b)

# @dispatch(int,int,int)
# def add(a,b,c):
#     print(a+b+c)

# add(2,3)
# add(2,3,4)



#### abstract class method 
## method without body



# from abc import ABC,abstractmethod

# class polygon(ABC):

#     @abstractmethod
#     def noofsides(self):
#         pass


# class triangle (polygon):

#     def noofsides(self):
#         print("i have 3 sides")
    

# class rectangle(polygon):

#     def noofsides(self):
#         print("i have 4 sides")

# obj1 = triangle()
# obj1.noofsides()

# obj2=rectangle()
# obj2.noofsides()

# def product(a, b):
# 	p = a * b
# 	print(p)


# def product(a, b, c):
# 	p = a * b*c
# 	print(p)

# product(4, 5, 5)


# print('####################################################')


# def add(datatype, *args):


# 	if datatype == 'int':
# 		answer = 0


# 	if datatype == 'str':
# 		answer = ''

# 	for x in args:


# 		answer = answer + x

# 	print(answer)



# add('int', 5, 6)


# add('str', 'Hi ', 'Geeks')

# print('####################################################')



# class Person(object):

#  	# __init__ is known as the constructor
#  	def __init__(self, name, idnumber):
#          self.name = name
#          self.idnumber = idnumber

#  	def display(self):
#          print(self.name)
#          print(self.idnumber)



# obj = Person("Khalid", 257853)

# # accessing public data member
# print("Name: ", obj.name)
# print("Id: ", obj.idnumber)


# # calling public member function of the class
# obj.display()

# program to illustrate protected access modifier in a class

# super class
# class Student:
# 	
# 	# protected data members
# 	_name = None
# 	_roll = None
# 	_branch = None
# 	
# 	# constructor
# 	def __init__(self, name, roll, branch): 
# 		self._name = name
# 		self._roll = roll
# 		self._branch = branch
# 	
# 	# protected member function 
# 	def _displayRollAndBranch(self):

# 		# accessing protected data members
# 		print("Roll: ", self._roll)
# 		print("Branch: ", self._branch)


# # derived class
# class Geek(Student):

# 	# constructor 
# 	def __init__(self, name, roll, branch): 
#          Student.__init__(self, name, roll, branch) 
# 		
# 	# public member function 
# 	def displayDetails(self):
#          # accessing protected data members of super class 
#          print("Name: ", self._name) 
# 		 # accessing protected member functions of super class 
#          self._displayRollAndBranch()

# # creating objects of the derived class	 
# obj = Geek("Ali", 1706256, "Information Technology") 

# # calling public member functions of the class
# obj.displayDetails() 



################################################
# program to illustrate private access modifier in a class

# class Geek:
	
# 	# private members
# 	__name = None
# 	__roll = None
# 	__branch = None

# 	# constructor
# 	def __init__(self, name, roll, branch): 
# 		self.__name = name
# 		self.__roll = roll
# 		self.__branch = branch

# 	# private member function 
# 	def __displayDetails(self):
# 		# accessing private data members
# 		print("Name: ", self.__name)
# 		print("Roll: ", self.__roll)
# 		print("Branch: ", self.__branch)
	
# 	# public member function
# 	def accessPrivateFunction(self):
# 		# accessing private member function
# 		self.__displayDetails() 

# 	# getter method for name
# 	def get_name(self):
# 		self.__name 
        
# 	# setter method name
# 	def set_name(self , name):
# 		self.__name = name 

# 	# getter method for roll
# 	def get_roll(self):
# 		self.__roll
        
# 	# setter method roll
# 	def set_roll(self , roll):
# 		self.__roll = roll 

# 	# getter method for branch
# 	def get_branch(self):
# 		self.__branch
        
# 	# setter method branch
# 	def set_branch(self , branch):
# 		self.__branch = branch 

             
# # creating object 
# obj = Geek("Osama", 1706256, "Information Technology")

# # calling public member function of the class
# obj.accessPrivateFunction()
