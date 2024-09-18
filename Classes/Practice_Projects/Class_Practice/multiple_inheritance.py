class Parent:

    def __init__(self, pname):
        self.pname = pname

    def show_name(self):
        return f"Parent name: {self.pname}"

    def parent_duties(self):
        return (f"it is the duty of the parent to ensure that the child \""
                f"attends school regularly with out fail.")

class Guardian:

    def __init__(self, gname):
        self.gname = gname

    def show_name(self):
        return f"Guardian Name: {self.gname}"

    def guardian_duties(self):
        return (f"it is the duty of the Guardian to ensure that the child \""
                f"attends school regularly with out fail in the absence of Parent.")

class Child(Parent, Guardian):

    def __init__(self,pname, gname, cname):
        super().__init__(pname)
        Guardian.__init__(self, gname)
        self.cname = cname

    def show_name(self):
        return f"Child Name: {self.cname}"

    def details(self):
        return f"Parent Name: {self.pname}, Guardian Name: {self.gname}"

Child_1 = Child("John", "David", "Elijah")
print(Child_1.show_name())
print(Child_1.details())
print(issubclass(Child, Parent))
print(issubclass(Child, Guardian))
print(issubclass(Guardian, Parent))
print(issubclass(Parent, Child))
print(Parent.show_name(Child_1))
print(Guardian.show_name(Child_1))
print(Child_1.parent_duties())
print(Child_1.guardian_duties())