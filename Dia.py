from typing import Any

class Employee:
    new_id = 1
    
    def _init_(self):
        self.id = Employee.new_id 
        Employee.new_id += 1
        
    def say_id(self):
        print(f"Mi id es: {self.id}")

Asael_Luces = Employee()
Citlali_Traidora = Employee()

Asael_Luces.say_id()
Citlali_Traidora.say_id()