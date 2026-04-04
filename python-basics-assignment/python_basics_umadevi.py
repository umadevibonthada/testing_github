name="umadevi"
age=30
height=5.4
is_Student=True
#Task1 : print all four values in single print line
print(name,age,height,is_Student)

#Task2 : Pring all four values in string formating

print (f"Name:{name} | Age:{age} | Height:{height} | Student:{is_Student}") # using  "f" string
print("Name:",name, "| Age:",age,"| Height:",height,"|Student:",is_Student)
print("Name: {} | Age: {} | Height: {}| Student: {}".format(name,age,height,is_Student)) #.format method
print(f" {"Name":<10} : {name} \n {"Age":<10} : {age} \n {"Height":<10} : {height} \n {"Student":<10} : {is_Student}")


#Task3 : Arithmetic Operations
age_months = age * 12
age_days_non_leap = age * 365
age_days_leap = age * 366
age_remainder = age% 7
print(age_remainder)

print("Age in months           : {} months".format(age_months))
print("Age in days (non-leap)  : {}".format(age_days_non_leap))
print("Age in days (leap year) : {}".format(age_days_leap))
print("Remainder when age ÷ 7  : {}".format(age_remainder))

print (f'''Age in months:{age_months} \n Age in days (non-leap) : {age_days_non_leap}\n 
Age in days (leap year):{age_days_leap} \n Remainder when age ÷ 7 :{age_remainder}''')
