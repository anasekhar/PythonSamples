"""
Decorator example
"""


def time_this(original_func):
    def new_function(*args,**kwargs):
        import datetime
	print args,kwargs
	before = datetime.datetime.now()
	print " Before starting orignal function"
	x = original_func(*args,**kwargs)
	print " After finishing original function"
	after = datetime.datetime.now()
	print "Elapsed time = {0}".format(after-before)
	#return x
    print "Just now calling new_fucntion"
    return new_function



@time_this
def func_a(stuff):
    import time
    print " Sleeping for 3 sec",stuff
    time.sleep(3)

func_a(1)
