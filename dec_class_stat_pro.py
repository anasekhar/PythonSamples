class MyClass(object):
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    def normal_method(*args,**kwargs):
        print("calling normal_method({0},{1})".format(args,kwargs))
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})".format(args,kwargs))
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})".format(args,kwargs))
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_property
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})".format(self,args,kwargs))
        self._some_property = args[0]
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_other_property

    @some_other_property.setter
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
	self._some_other_property= args[0]
	

obj = MyClass()

#print " obj.some_property", obj.some_property
#print " obj.some_other_property", obj.some_other_property
print " obj.some_property = very good"
obj.some_property="very good"
print " obj.some_other_property=very very good"
obj.some_other_property="vreryverygood","verybad","llllll"
print " obj.some_property====", obj.some_property
print " obj.some_other_property====", obj.some_other_property
