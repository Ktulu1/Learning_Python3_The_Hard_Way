#create a class - use object parameter for base class readability
class Parent(object):
    #define function to print
    def override(self):
        print("PARENT override()")
    #define function to print
    def implicit(self):
        print("PARENT implicit()")
    #define function to print
    def altered(self):
        print("PARENT altered()")
#create a class that inherits from Parent()
class Child(Parent):
    #define function to print
    def override(self):
        print("CHILD override()")
    #define function to print "CHILD", use super to call inherited function altered() from self, print "CHILD" again exclusively using the properties of Child()
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")
#instatiate objects dad and son    
dad = Parent()
son = Child()
#call specific functions in objects
dad.implicit()
son.implicit()
#call specific functions in objects
dad.override()
son.override()
#call specific functions in objects
dad.altered()
son.altered()
    