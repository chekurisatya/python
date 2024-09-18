class Parent():

    def __init__(self, pname):
        self.pname = pname
    # Parent's show method
    def display_Info(self,string):
        print(f"Inside Parent saying {string}")
    # Inherited or Sub class (Note Parent in bracket)

class Child(Parent):
    def __init__(self,pname, cname):
        super().__init__(pname)
        self.cname = cname
    # Child's show method
    def display_Info(self, string):
        print(f"Inside Child saying {string}")
        super().display_Info(string+'2')

    # Inherited or Sub class (Note Child in bracket)
class GrandChild(Child):
    def __init__(self,pname, cname, gcname):
        super().__init__(pname, cname)
        self.gcname = gcname
    # Child's show method
    def display_Info(self, string):
        print(f"Inside GrandChild saying {string}")
        super().display_Info(string+'1')

GC = GrandChild("CV Raju", "CSV Raju", "Aasritha")
GC.display_Info("Hello")