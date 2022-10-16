# 2022/10/16
'''
def format_name(f_name, l_name):
    print(f_name.title(), end = '')
    print(l_name.title())


format_name("heejeong ", "min")
'''

# 일수 알려주기

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
        print("Leap year.")
      else:
        return False
        print("Not leap year.")
    else:
        return True
        print("Leap year.")
  else:
    return False
    print("Not leap year.")

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    if month > 12 or month < 1:
        return "Invalid"
    
    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)