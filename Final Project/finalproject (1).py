# -*- coding: utf-8 -*-
"""FinalProject

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jJmp7P1Mr1uB4ZOPxU-o3uexjWbFHong
"""

class Employees():
    def __init__(self, name, lname, age, lang):
        self.first_name = name
        self.last_name=lname
        self.age = age
        self.lang= lang

    def print_employeeName(self):
      print(self.first_name + " " + self.last_name)

    def print_employeeAge(self):
      print(self.age)
        
    def print_lang(self):
        print(self.lang)

Serhat = Employees("Serhat","Dede", 21,"Turkish")
Zeynep=Employees("Zeynep", "Aslan" ,25, "Turkish " + " English")
Fatma= Employees("Fatma", "Sonmez",33, "German " + " Turkish")
Serdar=Employees("Serdar", "Vural" , 35, "English")

Serhat.print_employeeAge()
Serhat.print_employeeName()
Zeynep.print_employeeName


#Employee Languages

Serhat.print_lang()
Zeynep.print_lang()
Fatma.print_lang()
Serdar.print_lang()

class Managers(Employees):
  def __init__(self, name, lname, age, lang):
      self.first_name = name
      self.last_name=lname
      self.age = age
      self.lang= lang
      

  def print_manager_status(self):
        print(self.first_name + " " + self.last_name + " is " + str(self.age) + " and can speak " + self.lang)
        

Ali=Managers("Ali", "Yavuz" , 45, "Turkish "+ " English")
Melis=Managers("Melis", "Kaya",  43, "Turkish" + " English")
Jane= Managers("Jane", "Bulut", 52, "English " + " Italian")
David=Managers("David","Blake", 53, "English " + " Spanish")

Ali.print_manager_status()
Melis.print_manager_status()
Jane.print_manager_status()
David.print_manager_status()