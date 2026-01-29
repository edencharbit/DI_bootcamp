# Exercise 2: Working with JSON

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


data = json.loads(sampleJson)
salary_value = data["company"]["employee"]["payable"]["salary"]
print(f"The salary value is {salary_value}")
data["company"]["employee"]["birth_date"] = "1992-03-24"

with open("modified_employee.json", "w") as file:
    json.dump(data, file, indent=4)




