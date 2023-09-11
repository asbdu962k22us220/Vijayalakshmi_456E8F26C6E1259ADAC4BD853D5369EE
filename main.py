def CheckLeep(year):
  if((year%400==0)or
    (year%100!=0)and
    (year%4==0)):
    print("given year is a leep year")
  else: 
    print("given year is not a leep year")
year=int(input("enter the number:"))
CheckLeep(year)