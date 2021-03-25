def number(num1, num2, num3):
   list = [num1, num2, num3]
   list.sort() #sorted from the lowest number to the highest number

   if list[1] + 2 <= list[2] or list[0] + 2 <= list[1]:
      print("True")
   else:
      print("False")


number(1, 1, 1)
