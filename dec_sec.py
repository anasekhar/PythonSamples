"""
Decorator with arguments
"""

def do_something(*args,**kwargs):
    print args,kwargs

def out_dec(*out_args,**out_kwargs):
    def dec(fn):
	def decorated(*args,**kwargs):
	    do_something(*out_args,**out_kwargs)
	    return fn(*args,**kwargs)
	return decorated
    return dec


def out_dec1(fn):
    def decorator(*args,**kwargs):
	do_something(3,2,1)
	return fn(*args,**kwargs)
    return decorator

@out_dec(1,2,3)
def foo(a,b,c):
    print a
    print b
    print c

foo(10,20,30)


#################### 	Above code is equal to below code ###########
