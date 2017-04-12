def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through argv: ", arg)


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


test_var_args('yahoo', "hello", 'eggs')

greet_me(name="hello", last="world")

test_args_kwargs(*("a", 3 , 5))

kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)

test_args_kwargs(arg1=100, arg2=200, arg3=300)