import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL=""
MY_PASSWORD=""

now=dt.datetime.now()
date=now.day
month=now.month

# 2. Check if today matches a birthday in the birthdays.csv
birthday_data=pandas.read_csv("birthdays.csv")
data=birthday_data.to_dict(orient="records")
# print(data)
for i in data:
    # print(i["month"],i["day"])
    if(i["month"]==month and i["day"]==date):
        reciever_name=i["name"]
        reciever_email=i["email"]

        no=random.randint(1,3)
        with open(f"letter_templates/letter_{no}.txt") as file:
            file_data=file.read()
            # print(file_data)
            # print(type(file_data))
            file_data=file_data.replace("[NAME]",reciever_name)
            # print(file_data)

        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=reciever_email,
                msg=f"Subject:Happy Birthday\n\n{file_data}"
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




