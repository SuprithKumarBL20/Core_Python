#                                             #control flow of nested function
# def outer():
#     print("entering outer")
#     def inner():
#         print("entering inner")
#         print("processing")
#         print("leaving inner")
#     print("calling inner")
#     inner()
#     print("leaving outer")
# outer()
# print("Pgm Ended")

#                                              #Function Overloading 
# def fun1():
#     print("imside fun1")
# def fun1(a):
#     print("imside fun1 with arg",a)
# def fun1(a,b):
#     print("imside fun1")
# def fun1(a):
#     print("imside fun1 with arg",a)
# def fun1(a,b):
#     print("imside fun1 with 2 arg",a,b)
#      OUTPUT:ERROR
# ================================================================================
# def fun1():
#     print("imside fun1")
# def fun1(a):
#     print("imside fun1 with arg",a)
# def fun1(a):
#     print("imside fun1")
# def fun1(a):
#     print("imside fun1 with arg",a) 
# def fun1(a):
#     print("imside fun1 4")
#                         #      OUTPUT:imside fun1 4




# #                                       property decortor 
# class student :
#     def __init__(self):
#         self .__name=" "
#         @property
#         def dataAccess(self):
#             return self.__name
#         @dataAccess.setter
#         def dataAccess(self,value):
#             self.__name=value
# s1=student()
# s1.dataAccess="Rama"
# res1=s1.dataAccess
# print(res1)


# #=                                Creating object for child class/derived classs
# class Parent:
#     def __init__(self):
#         self.a=10
# class child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         self.b=20
# c1=child()
# print(c1.b)
# print(c1.a)

# #                                     Inheritance 
# class Plane:
#     def takeoff(self):
#         print("Plane is taking off")
#     def fly(self):
#         print("Plane is flying")
#     def land(self):
#         print("Plane is landing")
# class CargoPlane(Plane):
#     def carryCargo(self):
#         print("carrying cargo")
# class PassengerPlane(Plane):
#     def carryPassengers(self):
#         print("carrying passengers")
# class FighterPlane(Plane):
#     def carryWeapons(self):
#         print("carrying weapons")
# c=CargoPlane()
# p=PassengerPlane()
# f=FighterPlane()
# c.carryCargo()
# c.takeoff()
# c.fly()
# c.land()
# p.carryPassengers()
# p.takeoff()
# p.fly()
# p.land()
# f.carryWeapons()
# f.takeoff()
# f.fly()
# f.land()

# class Animal:
#     def eat(self):
#         print("Animal eats")
#     def sleep(self):
#         print("Animal sleeps")
#     def breath(self):
#         print("Animal breathes")
# class Dog(Animal):
#     pass

# class Deer(Animal):
#     pass
# f=Dog()
# d=Deer()
# f.eat()
# f.sleep()
# f.breath()
# d.eat()
# d.sleep()
# d.breath()


# #                                       Single Inheritance 
# class A:
#     def dispA(self):
#         print("inside dispa")
# class B(A):
#     def dispB(self):
#         print("isnide dispB")
# b1=B()
# b1.dispB()
# b1.dispA()


# #                                       Multi level Inheritance 
# class A:
#     def dispA(self):
#         print("inside dispa")
# class B(A):
#     def dispB(self):
#         print("isnide dispB")
# class C(B):
#     def dispC(self):
#         print("isnide dispB")
# c1=C()
# c1.dispC()
# c1.dispB()
# c1.dispA()

##                                          Multiple Inheritance
# class A:
#     def dispA(self):
#         print("inside dispa")
# class B():
#     def dispB(self):
#         print("isnide dispB")
# class C(A,B):
#     def dispC(self):
#         print("isnide dispB")
# c1=C()
# c1.dispC()
# c1.dispB()
# c1.dispA()

# #                                       Hierarchical Inheritance        
# class A:
#     def dispA(self):
#         print("inside dispa")
# class B(A):
#     def dispB(self):
#         print("isnide dispB")
# class C(A):
#     def dispC(self):
#         print("isnide dispB")
# c1=C()
# b1=B()
# c1.dispC()
# c1.dispA()
# b1.dispB()
# b1.dispA()

# #                                       Hybrid Inheritance
# #                          Hierarchical + Multiple Inheritance
# class A:
#     def dispA(self):
#         print("inside dispa")
# class B(A):
#     def dispB(self):
#         print("isnide dispB")
# class C(A):
#     def dispC(self):
#         print("isnide dispB")
# class D(B,C):
#     def dispD(self):
#         print("isnide dispB")
# d1=D()
# d1.dispD()
# d1.dispB()
# d1.dispA()
# d1.dispC()



