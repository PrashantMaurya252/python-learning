# username='Prashant'

# def func():
#     username="Maurya"
#     print(username)

# print(username)
# func()

x=99

# def f1():
#     x=88
#     def f2():
#         print(x)
#     return f2

# myResult=f1()
# myResult()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f=chaicoder(2)
print(f(3))
g=chaicoder(3)
print(g(3))
