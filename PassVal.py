import re
value=[]
passwords = [input("Please enter the 1st password option: "), input("Please enter the 2nd password option:  "), input("Please enter the 3rd password option:  "), input("Please enter the 4th password option: ")]

for password in passwords:
    if len(password)<8 or len(password)>12:
      print(password + " " + "Week pathword, enter the characters between 8-12")
      continue

    else:
        pass
    if not re.search("[a-z]",password):
      print(password + " - " + "Week pathword, enter the lower case characters")
      continue
    elif not re.search("[A-Z]", password):
      print(password + " - " + "Week pathword, enter the upper case characters")
      continue
    elif not re.search("[1-9]", password):
      print(password + " - " + "Week pathword, enter the numbers from 1 to 9")
      continue   
    elif not re.search("[#$@!%]", password):
      print(password + " - " + "Week pathword, password has to include one of the [#$@!%]")
      continue
    else:
        pass

    value.append(password)

print("Please use the following options for creating safe password: ", value)
