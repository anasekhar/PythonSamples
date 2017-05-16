"""
Decorator can be implented with class aswell
"""
def time_this(original_function):      
    print "decorating"                      
    def new_function(*args,**kwargs):
        print "starting timer"       
        import datetime                 
        before = datetime.datetime.now()                     
        x = original_function(*args,**kwargs)                
        after = datetime.datetime.now()                      
        print "Elapsed Time = {0}".format(after-before)      
        return x                                             
    return new_function 

def time_all_calss_methods(cls):
   class new_cls(object):
	def __init__(self,*args,**kwargs):
	    self.oInstance = cls(*args,**kwargs)
	def __getattribute__(self,s):
	    """
		This is called whenever any attribute of a newClass obj is accessed
	        This fucntion of get attribute off newcls
	 	if fails ten it retries to fet the att from self.Instance of dec class
		If it manges to fetch the attribute from self.oInstance the attribute is 
			instance method the 'time_this' is aplied
	    """ 
	    try:
		x = super(new_cls,self).__getarrtibute__(s)
	    except AttributeError:
		pass
	    else:
		return x
	    x = self.oInstance.__getattribute__(s)
	    if type(x) == type(self.__inti_):
		return time_this(x)
	    else:
		return x
   return new_cls


@time_all_calss_methods
class Foo(object):
    def a(self):
        print "entering a"
        import time
        time.sleep(3)
        print "exiting a"

oF = Foo()
oF.a()


