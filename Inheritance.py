# # Salary based on Heirarchy
# # 1. Single Inheritance
class person:
  def __init__(self,name):
    self.name=name
class employee(person):
  def __init__(self,name,salary):
    super().__init__(name)
    self.salary=salary

# 2. Multiple Inheritance
class job:
  def __init__(self,salary):
    self.salary=salary
class employeeperjob(employee,job):
  def __init__(self,name,salary):
    employee.__init__(self,name,salary)
    job.__init__(self,salary)

#  3. Multilevel Inheritance
class manager(employeeperjob):
  def __init__(self,name,salary,dept):
    employeeperjob.__init__(self,name,salary)
    self.dept=dept

# 4. Hierarchical Inhertance
class assistantmanager(employeeperjob):
  def __init__(self,name,salary,team_size):
    employeeperjob.__init__(self,name,salary)
    self.team_size=team_size
# 5. Hybrid Inheritance (Multiple +  Multilevel)
class seniormanager(manager,assistantmanager):
  def __init__(self,name,salary,dept,team_size):
    manager.__init__(self,name,salary,dept)
    assistantmanager.__init__(self,name,salary,team_size)
# Creating objects to show inheritance
# Single Inheritance
emp = employee("John", 40000)
print(emp.name, emp.salary)
# Multiple Inheritance
emp2 = employeeperjob("Alice", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.dep)

# Hierarchical Inheritance
asst_mgr = assistantmanager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = seniormanager("David", 70000, "Finance", 20)
print(sen_mgr.name,sen_mgr.salary,sen_mgr.dept,sen_mgr.team_size)
