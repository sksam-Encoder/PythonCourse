def cal(a, b):
    return print(sum((a, b)))


def func():
    print("this is an important function for execution")


try:
    cal('e', 2)
except Exception as e:
    print(e)
func()
