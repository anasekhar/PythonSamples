class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()


#a.go()  # go A go
#b.go()  # gp A go, go B go
#c.go()  # go A go,  go C go
#d.go()  # go A go, go B go,  go D go
e.go()  # go A go, go Bgo

#a.stop() #stop A
#b.stop() #stop A
#c.stop() #stop A, stop c stop
#d.stop() #stop A, stop D stop
#e.stop() #stp A stop

#a.pause()
#b.pause()
#c.pause()
#d.pause()
#e.pause()
