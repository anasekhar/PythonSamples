
class decorator_class():

    def __init__(self,org_fun):
        self.org_function = org_fun

    def __call__(self,*args,**kwargs):
        print("this is call menthod executed this beofre {}".format(self.org_function.__name__))
        return self.org_function(*args,**kwargs)


def decorator_func(org_fun):
    def wrapper(*args,**kwargs):
        print("this is dec function{}".format(args))
        return org_fun
    return wrapper()


@decorator_func
def display():
    print("this is dispaly")


display()

@decorator_class
def myname(firstname,lastname):
    print(firstname, lastname)


myname("sekhar","Anangi")

