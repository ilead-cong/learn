##########################################
#多继承
##########################################

class K1:
    def foo(self):
        print("K1-foo")

class K2:
    def foo(self):
        print("k2-foo")

    def bar(self):
        print("K2-bar")
    
class J1(K1, K2):
    pass

class J2(K1, K2):
    def bar(self):
        print("J2-bar")

class C(J1, J2):
    pass

print(C.__mro__)#查看类的继承关系
m = C()
m.foo()
m.bar()