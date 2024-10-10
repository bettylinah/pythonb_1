#it works with keys and value
#we start with key the followed by value as shown below
#ex
student={"name":"linah","age":"13","courses":["maths","eng"]}# it's not a must the key to be a string it can also be an interger or viceversa
print(student)
print(student["name"])
print(student["age"])
print(student["courses"])

student["adminsion"] ="1234"
print(student.get("adminsion","not found"))

student.update({"name":"max","age":17,"adminsion":1234})
print(student)

del student["age"]
print(student)
print(student.keys())
print(student.values())
print(student.items())

adminsion =student.pop("adminsion")
print(student)
print(adminsion)



#N/B
# FOR KEYS THAT ARE NOT FOUND
print(student.get("phone"))# this is used to idetify if a specific key is present in the dictionary variable

#OR
print(student.get("phone","not found"))