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

number = 3
for i in range(1,11):
    if i==5:
        continue
    print(number,'x',i,'=',number*i)