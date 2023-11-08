import pandas
from smtplib import SMTP
from datetime import datetime
# enter your email and app password
from data import my_email, my_password

now=datetime.now()
day=now.day
month=now.month
print(day)
print(month)


birthdays_df=pandas.read_csv("birthdays.csv")
print(birthdays_df)
birthdays_list=birthdays_df.to_dict(orient='records')
print(birthdays_list)

for i in range(len(birthdays_list)):
    if day == int(birthdays_list[i]['day']) and month == int(birthdays_list[i]['month']):
        print("today")

        name=birthdays_list[i]['name']
        email=birthdays_list[i]['email']
        year=birthdays_list[i]['year']
        month=birthdays_list[i]['month']
        day=birthdays_list[i]['day']

        with open("letter_1.txt") as data_file:
            file_content=data_file.read()
        print(file_content)
        ready_to_send=file_content.replace("[NAME]", name)
        print(ready_to_send)

        with SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f'subject: Happy Birthday\n\n{ready_to_send}')
    else:
        print("no birthdays")