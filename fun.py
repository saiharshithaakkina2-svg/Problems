# def greet ():
#     print("good afternoon")
# greet()    

# def multiply(a,b):
#     return a**b
# print(multiply(2,3))


# def profile(name , age):
#     print(name , age)
# profile( 22 , 'sai')     positional arguments these are

# def student(name, age, city):
#     print(name, age, city)

# student( age=22, city="Hyderabad" ,name="Ravi") these are keyword arguments

# def greet(name, message="Welcome"):
#     print(message, name)

# greet("sai")
# greet("sai", "Good evening")  default aruguments

 def total(*args):
     print(args)
     return sum(args)

 print(total(10, 20))
 print(total(3,4,5,6,7))


 def profile(**kwargs):
     print(kwargs)

 profile(name="Ravi", age=22)
 profile(name="Anu", city="Hyd", role="Dev")
