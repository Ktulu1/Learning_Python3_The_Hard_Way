class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    
    def inherit(self):
        print("CHILD inherits")
        super(Child, self).implicit()

dad = Parent()
son = Child()

#dad.implicit()
son.inherit()
