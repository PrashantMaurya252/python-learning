# 1st syntax
# def square(number):
#     return number**2

# result = square(4)
# print(result)


#  2nd sum of two numbers

# def add(a,b):
#     return a+b

# print(add(3,5))

# 3rd->Polymorphism->write a function multiplies two numbers,but also accept and multiply strings.

# def multiply(p1,p2):
#     return p1*p2

# print(multiply(8,5))
# print(multiply('a',5))
# print(multiply(5,'a'))

#  4th Create a function that returns both area and circumference of a circle given its radius
# import math

# def circle(radius):
#     area=math.pi*radius**2
#     circumference=2*math.pi*radius
#     return area,circumference

# a,c=circle(5)
# print("Area: ",round(a,2),"Circumference: ",round(c,2))

# 5th write a function to greet a user if no name provided then write  default name

# def greet(name="Prashant"):
#     return "Hello, "+name+" !"

# print(greet())

# 6th lambda function return a cube of a number
# cube = lambda x:x**3

# print(cube(3))

# 7th write a function that takes variable number of arguments and returns their sum

# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i*2)
#     return sum(args)


# print(sum_all(1,2,3))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))

# 8th Create a function that accepts any number of keyword arguments and prints them in the format key:value

# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# print_kwargs(power='lazer',name='shaktiman')
# print_kwargs(name='shaktiman')
# print_kwargs(name='shaktiman',power='lazer',enemy='Dr. Jackaal')

#  9th write a generator function that yields even numbers up to a specified limit.

# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i

# for num in even_generator(10):
#     print(num)


# 10th  recursive function factorial number

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
