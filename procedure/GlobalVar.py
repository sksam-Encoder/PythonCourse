# g = 10  # global
#
#
# def fun1(n):
#     # g = 1  # local
#     global g
#     g = g +40
#     print(g)
#     print(n, "print function printed")
# #   we cannot change  variable which is globally resolve
#
#
# fun1("hellow")
# # print(g)

# part 2 ---------------nested function--------------

# quiz case
x=11
def fun1():
    x = 20

    def innerfun():
        global x
        x = 10
        print("in the inner function x=", {x})

    print("before calling inner function x=", {x})
    innerfun()
    print("after calling inner function x=", {x})


fun1()
print(x)


#   declaring global keyword before varable it means  we want acess that globally