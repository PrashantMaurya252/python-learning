# 1st count positive numbers

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# count = 0
# for num in numbers:
#     if num > 0:
#         count +=1

# print(count,"count")

# sum of n even numbers

# n =10
# sum_even=0

# for i in range(1,n+1):
#     if i%2==0:
#         sum_even += i

# print(sum_even) 

# 3rd Print the multiplication table for a given number upto 10,but skip the fifth iteration

# number = 3
# for i in range(1,11):
#     if i==5:
#         continue
#     print(number,'x',i,'=',number*i)

# 4th reverse a string

# input_string='python'
# reversed_string=''

# for char in input_string:
#     reversed_string = char + reversed_string

# print(reversed_string)

# 5th first non repeated character in a string

# input_str='teeter'

# for char in input_str:
#     if input_str.count(char) == 1:
#         print("Char is: ",char)
#         break

# 6th factorial number using a while loop

# number = 5
# factorial=1

# while number > 0:
#     factorial = factorial * number
#     number = number-1

# print(factorial)

# 7th keep asking the user for input until they enter a number between 1 and 10.

# while True:
#     number=int(input("Enter value b/w 1 and 10 :"))
#     if 1<=number<=10:
#         print("thanks")
#         break
#     else:
#         print("Invalid number try again")

# 8th check prime number

# number= 28
# is_prime = True

# if number > 1:
#     for i in range(2,number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)

# 9th uniqueness checker

# items = ['apple','banana','orange','apple','mango']

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print('duplicate ',item)
#     unique_item.add(item)

# 10th Exponential Backoff -> Implement an exponential backoff strategy that doubles the wait time between, starting from 1 second, but stop after 5 retries

import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt",attempts + 1,"-wait time",wait_time,)
    time.sleep(wait_time)
    wait_time *=2
    attempts +=1
    