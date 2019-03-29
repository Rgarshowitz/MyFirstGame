class ParentClass:
    def __init__(self):
        self.a = 1
        print ('Parent Class object created')
    def someMethod(self):
        print ('hello')

class ChildClass(ParentClass):
        def __init__(self):
            print ('Child Class Object Created')

parent = ParentClass()
child = ChildClass()
