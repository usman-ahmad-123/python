class person:
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def display(self):
    print(self.name)
    print(self.id)
p1=person('osman',49)
p1.display()
class employee(person):
  def __init__(self,name,id,salary,post):
    super().__init__(name,id) 
    self.salary=salary
    self.post=post
  def display(self):
    print(self.name)
    print(self.id)
    print(self.post)
    print(self.salary)
p1=employee('usman',89,899,"erefsf")
p1.display()
print(p1)