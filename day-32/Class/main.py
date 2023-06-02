# 날짜 구하기
import datetime as dt

now = dt.datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)
weekday = now.weekday()
dic_weekday = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
# print(year+'-'+month+'-'+day+' '+dic_weekday.get(weekday))

import smtplib
import random 

# my_email = "hmin9988@gmail.com"
# my_pw = "eqcenjrsafhmldmk"
# google로 이메일 제공자와 smtp정보를 검색
# with smtplib.SMTP("smtp.gmail.com") as connection :
#     connection.starttls()
#     connection.login(user=my_email, password=my_pw)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="hjmlion@naver.com", 
#                         msg="Subject:hello\n\nThis is my body of email")
# connection.close()


#TODO. send a motivational quote via email on the current weekday


MY_EMAIL = "hmin9988@gmail.com"
MY_PW = "rkbryjyhmqsvxtnr"

now = dt.datetime.now()
day_of_weekday = now.weekday()

if day_of_weekday == 4:
    with open("day-32/Class/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PW)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="hjmlion@naver.com", msg=f"Subject: Friday Motivation\n\n{quotes}")
