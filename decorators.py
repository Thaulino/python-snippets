
# reference PEP318

# simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
    

@my_decorator
def f():
    print("hi")

# decorator with any kind of args and kwarg 
def my_any_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'start: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@my_any_decorator
def t():
    print("t")

@my_any_decorator
def r( rrr : str ):
    print(f"r{rrr}")


# configurable decorator 
# decorator with any kind of args and kwarg 

def my_any_decorator_with_para(para):
    def decorator_with_para(func):
        def wrapper(*args, **kwargs):
            print(f'para:{para}')
            print(f'start:{func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator_with_para


# equivalent to: func = decomaker(argA, argB, ...)(func)
# what happens -> call my_any_decorator_with_para with para("haha"), 
# take the result (decorator_with_para, which has para ("haha") stored as non locale state of closure) 
# and call it with func (t_with_para), the result of this is a wrapper function object with the closure state:
# func = t_with_para
# para = "haha"
#
@my_any_decorator_with_para("haha") 
def t_with_para():
    print("t")



# old school variant
#t_with_para = my_any_decorator_with_para(t_with_para, "haha")

#decorator used with classes 


def do_twice(func):
    def wrapper(self, x):
        func(self, x)
        func(self, x)
        return 

    return wrapper




class A_Foo:

    def __init__(self, ww:str):
        self.ww = ww

    @do_twice
    def do_something(self, x):
        print(f"{x},{self.ww}")


    #do_something = do_twice(do_something)







if __name__ == "__main__":

    #f()
    t_with_para()
    t()
    r("uuu")

    z = A_Foo("i am z!")
    z.do_something("dodoo")

    Y = A_Foo("i am Y!")
    Y.do_something("yyyyy")

    z.do_something("dooodoo2")